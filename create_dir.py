import os


def create(directory_path):
    os.makedirs(directory_path, exist_ok=True)
    return directory_path
