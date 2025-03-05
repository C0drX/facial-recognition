files_path = []

matched_path = []


def store_files_path(file_path):
    files_path.append(file_path)


def get_files_path():
    return files_path


def store_matched_path(matched_file_path):
    matched_path.append(matched_file_path)


def get_matched_path():
    return matched_path
