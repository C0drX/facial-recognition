import os
import cv2
import face_recognition

from adjust_tolerance import adjust_tolerance_based_on_quality
from check_blurriness import estimate_blurriness
from format_name import format_filename
from alive_progress import alive_bar


def find_matching_faces(sample_image_path, folder_path, base_tolerance=0.4):
    """
    Compare the sample image with images in a directory, matching based on facial encoding.

    Parameters:
    sample_image_path (str): Path to the sample image.
    folder_path (str): Path to the directory containing images to compare.
    tolerance (float): Threshold for face matching. Lower values are stricter. Default is 0.4.

    Returns:
    list: List of file paths for images that match the sample image.
    """
    matching_images = []

    # Load and encode the sample image
    sample_image = cv2.imread(sample_image_path)
    if sample_image is None:
        print(f"Error: Could not load sample image from {sample_image_path}")
        return []

    # Convert BGR to RGB (OpenCV loads images in BGR)
    sample_image_rgb = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
    sample_encoding = face_recognition.face_encodings(sample_image_rgb)

    if len(sample_encoding) == 0:
        print("Error: No face detected in the sample image.")
        return []

    sample_encoding = sample_encoding[0]

    files_list = os.listdir(folder_path)

    print()
    print(f"Matching sample through {len(files_list)} faces....")
    with alive_bar(len(files_list)) as bar:
        # Iterate through the folder and compare each image with the sample
        for image_file in files_list:
            image_path = os.path.join(folder_path, image_file)

            # Only process image files
            if not image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # print("File does not contain a proper extension, Skipping !")
                bar(skipped=True)
                continue

            # Load and encode the current image
            current_image = cv2.imread(image_path)
            current_image_rgb = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
            current_encodings = face_recognition.face_encodings(
                current_image_rgb)

            if len(current_encodings) == 0:
                # print(f"No face detected in {image_file}, Skipping.")
                bar(skipped=True)
                continue

            # # Assess the quality of the current image (blurriness)
            blurriness_score = estimate_blurriness(current_image)
            # print(f"Blurriness score for {image_file}: {blurriness_score}")

            # # Adjust tolerance based on image quality
            adjusted_tolerance = adjust_tolerance_based_on_quality(
                blurriness_score, base_tolerance)
            # print(f"Adjusted tolerance for {image_file}: {adjusted_tolerance}")

            # Compare each detected face with the sample
            for face_encoding in current_encodings:
                match_results = face_recognition.compare_faces(
                    [sample_encoding], face_encoding, tolerance=adjusted_tolerance)
                face_distance = face_recognition.face_distance(
                    [sample_encoding], face_encoding)[0]

                if match_results[0]:
                    # print(
                    #     f"Match found in {format_filename(image_file)} with distance: {face_distance:.2f}")
                    matching_images.append(format_filename(image_file))
                else:
                    # print(
                    #     f"No match for {format_filename(image_file)}. Distance: {face_distance:.2f}")
                    pass

            bar()

    return matching_images
