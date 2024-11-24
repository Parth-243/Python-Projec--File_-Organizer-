from organizer.organizer import organize_files_by_extension

def main():
    directory_path = input("Enter the directory path to organize: ")
    organize_files_by_extension(directory_path)

if __name__ == "__main__":
    main()
