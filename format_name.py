import os
from pathlib import Path


def format_filename(filename):
    base_filename = os.path.split(filename)[1]
    file_extension = Path(base_filename).suffix
    raw_name = base_filename.split("+")[0]
    formatted_name = raw_name + file_extension
    return formatted_name
