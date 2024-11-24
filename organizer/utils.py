import os

def create_folder_if_not_exists(folder_path):
    os.makedirs(folder_path, exist_ok=True)
