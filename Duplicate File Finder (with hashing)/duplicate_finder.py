#!/usr/bin/env python3

"""Duplicate File Finder (CLI Tool)

This script scans a directory and identifies duplicate files based on content.

Workflow:
1. Files are grouped by size to quickly eliminate non-duplicates.
2. Only groups with matching sizes are hashed using MD5.
3. Files with identical hashes are reported as duplicates.

Features:
- Efficient duplicate detection using size pre-filtering
- Content-based comparison using hashing
- CLI support for specifying target directory

Limitations:
- Only scans the top-level directory (non-recursive)
- Uses MD5 (fast but not cryptographically secure, acceptable for this use case)

Usage:
    python duplicate_finder.py --path ./your-folder
"""

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


def group_by_hash(files, hashed_files):
    for file in files:
        #modern approach for large files
        with open(file, "rb") as f:
            file_hash = hashlib.file_digest(f,'md5').hexdigest()
        if file_hash not in hashed_files:
            hashed_files[file_hash] = []
        hashed_files[file_hash].append(file)


def main(path):
    #path check

    if not args.path.exists() or not args.path.is_dir():
        print("Please provide a valid folder path.")
        return

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
                group_by_hash(group, hashed_files)

    show_results(hashed_files)                 

main(args.path)