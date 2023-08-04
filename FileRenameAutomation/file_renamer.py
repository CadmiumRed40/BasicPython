import os

def rename_files(folder_path, prefix):
    #getting a list of all files in the folder
    files = os.listdir(folder_path)

    #filter out the subdirectories, if any exist
    files = [f for f in files if os.path.isfile(os.path.join(folder_path,f))]

    #starting the sequential number from 1
    count = 1

    #iterate over the files and rename them
    for file_name in files:
        #getting file extension
        _, ext = os.path.splitext(file_name)

        #new file name with the prefix and sequential number
        new_name = f"{prefix}_{count}{ext}"

        #full path of the file to rename
        old_path = os.path.join(folder_path, file_name)

        #full path of the new file name
        new_path = os.path.join(folder_path, new_name)

        #rename the file
        os.rename(old_path, new_path)

        #incremement the count for the next file
        count += 1

    if __name__ == "__main__":
        folder_path = input("Enter the folder path where files need to be renamed: ")
        prefix = input("Enter the prefix for the new file names: ")
        rename_files(folder_path, prefix)
        print("Files have been renamed successfully!")
