import os

def rename_files(folder_path, prefix):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print("Error: Folder path does not exist.")
        return

    # Get a list of all files in the folder and sort them
    files = os.listdir(folder_path)
    files.sort()

    # Filter out subdirectories, if any
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Start the sequential number from 1
    count = 1

    print("Files in the folder before renaming:")
    print(files)

    # Iterate over the files and rename them
    for file_name in files:
        # Get the file extension
        _, ext = os.path.splitext(file_name)

        # New file name with the prefix and sequential number
        new_name = f"{prefix}_{count}{ext}"

        # Full path of the file to rename
        old_path = os.path.join(folder_path, file_name)

        # Full path of the new file name
        new_path = os.path.join(folder_path, new_name)

        print(f"Renaming {old_path} to {new_path}")

        # Rename the file
        os.rename(old_path, new_path)

        # Increment the count for the next file
        count += 1

    # Get the updated list of files after renaming
    files_after_renaming = os.listdir(folder_path)
    files_after_renaming.sort()

    print("Files in the folder after renaming:")
    print(files_after_renaming)

if __name__ == "__main__":
    folder_path = input("Enter the folder path where files need to be renamed: ")
    prefix = input("Enter the prefix for the new file names: ")
    rename_files(folder_path, prefix)
    print("Files have been renamed successfully!")
