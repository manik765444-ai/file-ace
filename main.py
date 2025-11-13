# main.py

import os
import shutil


def organize_files(directory_path, extensions):
    """
    Organize files in a directory based on their extensions.

    Args:
    directory_path (str): The path to the directory containing the files.
    extensions (dict): A dictionary where keys are file extensions and values are destination directories.

    Returns:
    None
    """
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        for file in os.listdir(directory_path):
            _, ext = os.path.splitext(file)
            if ext in extensions:
                src_path = os.path.join(directory_path, file)
                dest_path = os.path.join(extensions[ext], file)
                os.makedirs(extensions[ext], exist_ok=True)
                shutil.move(src_path, dest_path)
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(f"Permission denied: {directory_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to organize files in a specified directory.

    Returns:
    None
    """
    directory_path = input("Enter the directory path: ")
    file_extensions = {
        ".txt": "TextFiles",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".png": "Images",
        ".py": "PythonFiles",
        ".csv": "DataFiles"
    }

    organize_files(directory_path, file_extensions)
    print("File organization complete.")


if __name__ == "__main__":
    main()