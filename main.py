import shutil
import os
import face_crop
import face_rec
import path_gen
import storage
import create_dir
import operations_file

from colorama import Fore, Style

# * <-------------Take input from user and scrap face for Sample Image ---------------->


def take_sample_image():
    return str(input("Enter the path of the sample image : "))


while True:
    sample_image = take_sample_image()
    if os.path.exists(sample_image):  # file or directory exists
        pass
    else:
        print("File path is not valid !!")
        continue
    scrap_sample = face_crop.crop_sample_face(
        sample_path=sample_image, output_width=400, output_height=400)
    if not scrap_sample == 400:
        break
    else:
        pass


# * <-------------Take input from user for dataset folder ---------------->
def take_data_folder_path():
    return str(input("Enter the path of the data folder : "))


while True:
    data_folder = take_data_folder_path()
    if os.path.exists(data_folder):  # file or directory exists
        break
    else:
        print("Data folder path is not valid !!")
        pass


# * <------------- Scrap Faces From Dataset Folder Images ---------------->
scrap_directory = face_crop.crop_faces(folder_path=data_folder,
                                       output_width=400, output_height=400)


# * <------------- Compare Between Dataset Images and Sample Image ---------------->
matches = face_rec.find_matching_faces(
    sample_image_path=scrap_sample, folder_path=scrap_directory, base_tolerance=0.475)


# * <------------- Get Path of Every Image File Found in Dataset Folder ---------------->
files = storage.get_files_path()


# * <------------- Get Real Path of Matched Image ---------------->
#! it is used for program to generate real path. because,
#! this code uses a different directory to store and comparing faces.

matched_path = path_gen.find_paths_from_filenames(
    paths_list=files, filenames_list=matches)


# *<--------------------------- Filter and save original path of matched files --------------------------->

for index, (filename, path) in enumerate(matched_path.items(), start=1):
    if path:
        storage.store_matched_path(matched_file_path=path)
    else:
        pass

print()
print(
    f"We found match for {len(storage.get_matched_path())} files with your given sample")

#! <------------------------- DELETE SCRAP DIRECTORY USED FOR SCRAPPING FACES -------------------------->
shutil.rmtree(path="scrap")

# * <------------------------- MENU FOR USER -------------------------->

while True:
    menu_options = ('0', '1', '2', '3', '4', '5')
    print()
    print(Fore.CYAN + "[1] Show matched files")
    print(Fore.CYAN + "[2] Copy matched files to another folder")
    print(Fore.CYAN + "[3] Move matched files to another folder")
    print(Fore.CYAN + "[4] Open matched files")
    print(Fore.CYAN + "[5] Delete matched files")
    print(Fore.CYAN + "[0] Exit the program")
    print(Style.RESET_ALL)
    option = str(input("Choose an option : "))

    #!! if user enters something which is not available in options menu
    if not option in menu_options:
        print()
        print("option not available, please choose a correct option")
        continue

    #!! simply prints matched files path to the console
    if option == '1':
        operations_file.showFiles(storage.get_matched_path())

    #!! if user wants to copy matched files to a different directory
    if option == '2':
        print()
        print("Enter the path where do you want to copy files")
        copy_folder_path = str(input("enter the path : "))
        if os.path.exists(copy_folder_path):  # file or directory exists
            pass
        elif copy_folder_path == "":
            print()
            print("Path cannot be empty, please enter a valid path...")
            continue
        else:
            print()
            print("Couldn't find specified directory, creating one...")
            # continue
        print()
        print("Enter the name for new folder")
        copy_folder_name = str(input("enter the name : "))
        copy_dir_name = create_dir.create(directory_path=os.path.join(
            copy_folder_path, copy_folder_name))
        operations_file.copyFiles(
            source_files=storage.get_matched_path(), destination_path=copy_dir_name)

    #!! if user wants to move matched files to a different directory
    if option == '3':
        print()
        print("Enter the path where do you want to move files")
        move_folder_path = str(input("enter the path : "))
        if os.path.exists(move_folder_path):  # file or directory exists
            pass
        else:
            print()
            print("Couldn't find specified directory, creating one...")
            # continue
        print()
        print("Enter the name for new folder")
        move_folder_name = str(input("enter the name : "))
        move_dir_name = create_dir.create(directory_path=os.path.join(
            move_folder_path, move_folder_name))
        while True:
            print()
            move_confirmation = str(
                input("are you sure want to move your files [confirm] : "))
            if move_confirmation == 'confirm':
                operations_file.copyFiles(
                    source_files=storage.get_matched_path(), destination_path=move_dir_name)
                break
            elif move_confirmation == 'back':
                break
            else:
                print(
                    'please type [confirm] to continue or [back] to go back')

    #!! if user wants to open matched files in a different window
    if option == '4':
        open_matched_list = storage.get_matched_path()
        if len(open_matched_list) > 20:
            while True:
                print()
                print(
                    Fore.YELLOW + f"**There is a large number of data (i.e {len(open_matched_list)} files) which can cause unstablity to your system.")
                print(Style.RESET_ALL)
                open_file_confirmation = str(
                    input("are you sure want to continue [confirm] : "))
                if open_file_confirmation == 'confirm':
                    operations_file.open_files(files_list=open_matched_list)
                    break
                elif open_file_confirmation == 'back':
                    break
                else:
                    print(
                        'please type [confirm] to continue or [back] to go back')
        else:
            operations_file.open_files(files_list=open_matched_list)

    #!! if user wants to delete matched files from their original directory
    if option == '5':
        while True:
            print()
            print(
                Fore.RED + f"**This will cause complete removal of matched files. Think again !!!")
            print(Style.RESET_ALL)
            delete_file_confirmation = str(
                input("are you still want to continue [confirm] : "))
            if delete_file_confirmation == 'confirm':
                operations_file.deleteFiles(
                    files_path=storage.get_matched_path())
                break
            elif delete_file_confirmation == 'back':
                break
            else:
                print(
                    'please type [confirm] to continue or [back] to go back')

    #!! simply closes the program
    if option == '0':
        while True:
            print()
            exit_confirmation = str(
                input("are you sure want to exit [confirm] : "))
            if exit_confirmation == 'confirm':
                exit()
            elif exit_confirmation == 'back':
                break
            else:
                print(
                    'please type [confirm] to continue or [back] to go back')
