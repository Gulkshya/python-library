import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)
        if os.path.isfile(source):
            ext = filename.split('.')[-1].lower()
            dest_dir = os.path.join(folder_path, ext + "_files")

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            shutil.move(source, os.path.join(dest_dir, filename))

    print("Files organized successfully.")

folder = input("Enter the full folder path to organize: ")
organize_files(folder)
