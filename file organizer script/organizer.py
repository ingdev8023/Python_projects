#!/usr/bin/env python3

"""Problem:
Organize files in a folder_path by type"""

import os
from pathlib import Path
import shutil

folder_path = Path.cwd()

files_type = {
    '.jpg': 'images',
    '.png': 'images',
    '.mp3': 'music',
    '.mp4': 'video',
    '.pdf': 'documents'
}

counter = 0

def file_work(file,folder):
    
    extension = file.suffix
     
    if extension in files_type:
        #renaming the files
        new_name= folder.joinpath('test' + files_type[extension] + extension)
        file.rename(new_name)
        #creating the new folders
        new_folder = folder.joinpath(files_type[extension])
        new_folder.mkdir(exist_ok=True)
        #moving the files
        shutil.move(new_name, new_folder)
        
    else:
        print(f"file extension {file.suffix} not workable")

    



def main(folder_path):    
    for files in folder_path.iterdir():
        if files.is_dir():
            for file in files.iterdir():
                if file.is_file():
                    file_work(file,files)

     

main(folder_path)

#old school and just strings with listdir     
""" for dir in dir_path:
        if os.path.isdir(os.path.join(folder_path, dir)):
            for file in os.listdir(os.path.join(folder_path, dir)):
                print("It's a File")
        else:
            print("It's not a directory (or doesn't exist).") """

#print(os.path.join(folder_path, dir))







