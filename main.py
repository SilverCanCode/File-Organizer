
import os
import shutil
from extention_map import extension_map  # Ensure this is a dictionary


def organize_files(path):
    # Change the working directory to the provided path
    try:
        os.chdir(path)
    except Exception as e:
        print(f"Error changing directory: {e}")
        return

    # Create folders based on the extension_map if they don't exist
    for folder_name in extension_map.values():
        folder_path = os.path.join(path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # List all files in the directory
    try:
        check = os.listdir(path)
    except Exception as e:
        print(f"Error listing directory contents: {e}")
        return

    # Iterate over each file in the directory
    for file_name in check:
        file_path = os.path.join(path, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        basename, extension = os.path.splitext(file_name)

        # Check if the file's extension is in the extension_map and move it
        if extension in extension_map:
            folder_name = extension_map[extension]
            target_folder_path = os.path.join(path, folder_name)
            try:
                shutil.move(file_path, os.path.join(target_folder_path, file_name))
                print(f"Moved: {file_name} -> {folder_name}")
            except Exception as e:
                print(f"Error moving file {file_name}: {e}")

    print("Files have been organized.")


inp = input(
    "Enter your path name where all your files are present: (Ex - C:\\Users\\[Your "
    "username]\\OneDrive\\Desktop\\Python Projects\\FileOrganizer ) [Put double slash]: ")
organize_files(inp)
