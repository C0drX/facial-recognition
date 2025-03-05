import os


def build_filename_to_path_map(paths_list):
    # Create a dictionary that maps filenames (without extension) to their absolute paths
    filename_to_path = {}
    for path in paths_list:
        filename_without_extension = os.path.splitext(os.path.basename(
            path))[0]  # Extract the filename without the extension
        filename_to_path[filename_without_extension] = path
    return filename_to_path


def find_paths_from_filenames(paths_list, filenames_list):
    # Build the mapping from filenames (without extension) to their absolute paths
    filename_to_path = build_filename_to_path_map(paths_list)

    # For each filename in filenames_list (ignoring extension), find the corresponding path
    result = {}
    for full_filename in filenames_list:
        filename_without_extension = os.path.splitext(
            full_filename)[0]  # Remove extension from filename
        if filename_without_extension in filename_to_path:
            result[full_filename] = filename_to_path[filename_without_extension]
        else:
            # If the filename is not found, return None
            result[full_filename] = None
    return result


# Example usage
# paths_list = [
#     "assets\IMG_8978.jpg",
#     "assets\IMG_8980.jpg",
#     "assets\IMG_9019.jpg",
#     "assets\IMG_9008.jpg",
#     "assets\IMG_9005.jpg",
#     "assets\IMG_9006.jpg",
#     "assets\IMG_9051.jpg",
#     "assets\IMG_9065.jpg",
#     "assets\IMG_9007.jpg"
# ]

# filenames_list = [
#     "IMG_9051.png",
#     "IMG_9065.exl",
#     "IMG_9005.exe"  # This file doesn't exist in paths_list
# ]

# Get the respective paths for the filenames in filenames_list
# result = find_paths_from_filenames(paths_list, filenames_list)

# Print the results
# for filename, path in result.items():
#     if path:
#         print(f"Filename '{filename}' found at: {path}")
#     else:
#         print(f"Filename '{filename}' not found.")
