#!/usr/bin/env python3

from pathlib import Path
import argparse


parser = argparse.ArgumentParser(description="find duplicate files")

parser.add_argument(
    "--path",
    type=Path,
    default=Path.cwd(),
    help="Folder to review"
)

args = parser.parse_args()

files_dict = {}

def show_results(files_dict):
    for extension in files_dict:
        for size in files_dict[extension]:
            if len(files_dict[extension][size]) > 1:
                print(f'Possible duplicates, same extension{extension} and size={size} bytes:')
                for file in files_dict[extension][size]:
                    print(f'-{file}')
            else:
                print("No possible duplicates found")

def main(path):
    for file in path.iterdir():
        size = file.stat().st_size
        extension = file.suffix.lower()
        if file.is_file():
            if extension not in files_dict:
                files_dict[file.suffix] = {}
            if size not in files_dict[extension]:
                files_dict[extension][size] = []         
        
            files_dict[extension][size].append(file)
    show_results(files_dict)                 

main(args.path)