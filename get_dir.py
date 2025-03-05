import os


def get_all_file_paths(root_dir):
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_paths.append(os.path.join(dirpath, filename))
    return file_paths


# Example usage
root_directory = 'assets'  # Replace with the path to your folder
file_paths = get_all_file_paths(root_directory)

# Print all file paths
for path in file_paths:
    print(path)
