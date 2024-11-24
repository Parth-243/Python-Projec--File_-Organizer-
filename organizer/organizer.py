# organizer/organizer.py

import os
import shutil
from organizer.utils import create_folder_if_not_exists

EXTENSION_FOLDERS = {
    "Music": ["mp3", "wav", "flac", "aac", "ogg"],
    "Videos": ["mp4", "mkv", "mov", "avi"],
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tiff"],
    "Documents": ["pdf", "docx", "doc", "txt", "xlsx", "pptx"],
    "Archives": ["zip", "tar", "gz", "rar"],
}

def get_folder_for_extension(extension):
    for folder, extensions in EXTENSION_FOLDERS.items():
        if extension in extensions:
            return folder
    return extension

def organize_files_by_extension(directory):
    
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1][1:].lower() or "no_extension"
        
        target_folder = get_folder_for_extension(file_extension)
        target_folder_path = os.path.join(directory, target_folder)
        
        create_folder_if_not_exists(target_folder_path)

        shutil.move(file_path, os.path.join(target_folder_path, filename))
        print(f"Moved '{filename}' to '{target_folder_path}'.")

    print("Files organized successfully!")
