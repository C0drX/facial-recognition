import shutil
import os
import cv2

from alive_progress import alive_bar


def showFiles(file_list):
    for index, file in enumerate(file_list, start=1):
        print(f"{index}. {file}")


def copyFiles(source_files, destination_path):
    copy_file_length = len(source_files)
    print()
    print(f"Copying {copy_file_length} files to {destination_path} ...")
    with alive_bar(total=copy_file_length) as bar:
        for file in source_files:
            try:
                shutil.copy(src=file, dst=destination_path, )
            except shutil.Error as e:
                print(
                    f"File {os.path.basename(file)} already exists in {destination_path}, Skipping !!")
            bar()
    return


def moveFiles(source_files, destination_path):
    move_file_length = len(source_files)
    print()
    print(f"Moving {move_file_length} files to {destination_path} ...")
    with alive_bar(total=move_file_length) as bar:
        for file in source_files:
            try:
                shutil.move(src=file, dst=destination_path)
            except shutil.Error as e:
                print(
                    f"File {os.path.basename(file)} already exists in {destination_path}, Skipping !!")
            bar()
    return


def deleteFiles(files_path):
    delete_file_length = len(files_path)
    print()
    print(f"Deleting {delete_file_length} files...")
    with alive_bar(total=delete_file_length) as bar:
        for file in files_path:
            try:
                os.remove(file)
            except shutil.Error as e:
                print(
                    f"Cannot delete file {os.path.basename(file)} may be it is not available, Skipping !!")
            bar()
    return


def open_files(files_list):
    for index, file in enumerate(files_list, start=1):
        try:
            img = cv2.imread(file, cv2.IMREAD_COLOR)
            resized_face = cv2.resize(img, (400, 400))
            cv2.imshow(f'img {index}', resized_face)
        except:
            print(f"Couldn't open file {os.path.basename(file)}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return
