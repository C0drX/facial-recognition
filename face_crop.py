import os
import time
import cv2
import dlib
import storage

from pathlib import Path
from create_dir import create
from alive_progress import alive_bar

# Load the pre-trained face detector from dlib
detector = dlib.get_frontal_face_detector()


# # Provide the path of the Directory
# folder_path = 'assets'


# # Desired output resolution (e.g., 200x200 pixels)
# output_width, output_height = 400, 400


def crop_faces(folder_path, output_width=200, output_height=200):

    scrap = 'scrap'

    scrap_dir = create(directory_path=scrap)

    for dirpath, dirnames, filenames in os.walk(folder_path):
        print()
        print(f"Found {len(filenames)} items in directory : {dirpath}")
        print()
        print("Scrapping all the faces from images found in directory...")
        with alive_bar(total=len(filenames)) as bar:
            for filename in filenames:
                image_path = os.path.join(dirpath, filename)
                file_name = Path(image_path).stem

                # Only process image files
                if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    print("File does not contain a proper extension, Skipping !")
                    bar(skipped=True)
                    continue

                storage.store_files_path(image_path)

                # Load the image
                img = cv2.imread(image_path)

                # Convert image to grayscale (dlib works better with grayscale images)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Detect faces using dlib
                faces = detector(gray)

                # Loop through detected faces and crop them
                for i, face in enumerate(faces):
                    x, y, w, h = face.left(), face.top(), face.width(), face.height()

                    # Add padding to include full face (if cropping is too tight)
                    padding = 30
                    x1, y1, x2, y2 = max(x - padding, 0), max(y - padding, 0), min(x +
                                                                                   w + padding, img.shape[1]), min(y + h + padding, img.shape[0])

                    # Crop the face
                    face_img = img[y1:y2, x1:x2]

                    # Resize the cropped face to the desired resolution
                    resized_face = cv2.resize(
                        face_img, (output_width, output_height))

                    # Save the cropped face to a file
                    cv2.imwrite(
                        f'{scrap}\{file_name}+{i}.jpg', resized_face)

                    # print(
                    #     f"Faces successfully scrapped from file : {image_path}")
                bar()
            # Optionally display the cropped face
            # cv2.imshow(f'{image_file}+{i}', face_img)
    return scrap


def crop_sample_face(sample_path, output_width=200, output_height=200):

    sample = 'scrap\sample'
    sample_image = 'scrap\sample\sample.jpg'
    sample_dir = create(directory_path=sample)

    # Only process image files
    if not sample_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Sample image does not contain a proper extension !")
        return

    # Load the image
    img = cv2.imread(sample_path)

    # Convert image to grayscale (dlib works better with grayscale images)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces using dlib
    faces = detector(gray)

    if len(faces) == 0:
        print("No face is detected, Please try with another sample !")
        return 400

    if len(faces) > 1:
        print("Multiple faces are detected in sample image, Please try with another sample containing single face !")
        return 400

    # Loop through detected faces and crop them
    for i, face in enumerate(faces):
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Add padding to include full face (if cropping is too tight)
        padding = 30
        x1, y1, x2, y2 = max(x - padding, 0), max(y - padding, 0), min(x +
                                                                       w + padding, img.shape[1]), min(y + h + padding, img.shape[0])

        # Crop the face
        face_img = img[y1:y2, x1:x2]

        # Resize the cropped face to the desired resolution
        resized_face = cv2.resize(
            face_img, (output_width, output_height))

        # Save the cropped face to a file
        cv2.imwrite(
            f'{sample}\sample.jpg', resized_face)

        print(f"Sample face successfully scrapped from file : {sample_path}")

    return sample_image
