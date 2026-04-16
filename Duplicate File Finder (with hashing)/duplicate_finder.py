#!/usr/bin/env python3

from pathlib import Path
import argparse
import hashlib

parser = argparse.ArgumentParser(description="find duplicate files")

parser.add_argument(
    "--path",
    type=Path,
    default=Path.cwd(),
    help="Folder to review"
)

args = parser.parse_args()

def show_results(hashed_files):
    duplicates_found = False        
    for file_hash, files in hashed_files.items():
        if len(files) > 1:
            duplicates_found = True
            print(f'Duplicates files found: \nHash: {file_hash}\n')
            for file in files:
                print(f'-{file}')
    if not duplicates_found:
        print("No duplicates Found")


def group_by_hash(files,hashed_files):
    for file in files:
        with open(file, "rb") as f:
            data = f.read()
            file_hash = hashlib.md5(data).hexdigest()
        if file_hash not in hashed_files:
            hashed_files[file_hash] = []
        hashed_files[file_hash].append(file)


def main(path):
    #main vars

    files_dict = {}
    hashed_files = {}

    #checking files in the folder

    for file in path.iterdir():
        

        if file.is_file():
            size = file.stat().st_size
            extension = file.suffix.lower()
            if extension not in files_dict:
                files_dict[extension] = {}
            if size not in files_dict[extension]:
                files_dict[extension][size] = []         

            files_dict[extension][size].append(file)

    #group and check by size

    for extension in files_dict:
        for size in files_dict[extension]:
            group = files_dict[extension][size]
            if len(group) > 1:
                group_by_hash(group,hashed_files)

    show_results(hashed_files)                 

main(args.path)