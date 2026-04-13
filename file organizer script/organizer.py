#!/usr/bin/env python3

"""Recursively organize files by extension.

This script scans the current working directory and its subfolders,
moves supported files into category folders based on extension,
and avoids overwriting files by adding a numeric suffix when needed.

Supported categories:
- images: .jpg, .png
- music: .mp3
- video: .mp4
- documents: .pdf
"""

from pathlib import Path


folder_path = Path.cwd()

files_type = {
    '.jpg': 'images',
    '.png': 'images',
    '.mp3': 'music',
    '.mp4': 'video',
    '.pdf': 'documents'
}



def file_work(file_path,current_folder):
    
    extension = file_path.suffix.lower()
    category = files_type.get(extension)
    stem = file_path.stem
    if category:
        #creating the new folders
        target_folder = current_folder / category
        target_folder.mkdir(exist_ok=True)      

        #renaming the files
        destination = target_folder / file_path.name
        counter = 1
        while destination.exists():
            new_name = f"{stem}_{counter}{extension}"
            destination = target_folder / new_name
            counter += 1      
        file_path.rename(destination)               
    else:
        print(f"file extension {file_path.suffix} not workable")

    
def main(folder_path):    
    for file in folder_path.iterdir():
        if file.is_file():
            file_work(file,folder_path)
        if file.is_dir() and file.name not in files_type.values():
            main(file)

     

main(folder_path)