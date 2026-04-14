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
import argparse

parser = argparse.ArgumentParser(description="Organize files by type")

parser.add_argument(
    "--path",
    type=Path,
    default=Path.cwd(),
    help="Folder to organize"
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Show what would happen without moving files"
)

args = parser.parse_args()

FILES_TYPE = {
    '.jpg': 'images',
    '.png': 'images',
    '.mp3': 'music',
    '.mp4': 'video',
    '.pdf': 'documents'
}

summary = {
    'moved_count': 0,
    'skipped_count' :0,
    'renamed_count' : 0
}



def organize_file(file_path,current_folder, summary, dry_run):
    extension = file_path.suffix.lower()
    category = FILES_TYPE.get(extension)
    stem = file_path.stem

    if category:
        #creating the new folders
        target_folder = current_folder / category              

        #renaming the files
        destination = target_folder / file_path.name
        counter = 1
        was_renamed = False
        while destination.exists():
            new_name = f"{stem}_{counter}{extension}"
            destination = target_folder / new_name
            counter += 1  
            was_renamed = True
        if dry_run:
            if not target_folder.exists():
                print(f"Would create folder: {target_folder}")
                print(f"Would move: {file_path} -> {destination}")
            else:
                target_folder.mkdir(exist_ok=True)
                file_path.rename(destination)
        
        if was_renamed:
            summary['renamed_count'] += 1    
        
        summary['moved_count'] += 1               
    else:
        summary['skipped_count'] += 1
        print(f"file extension {file_path.suffix} not workable")
        return

def main(path,summary,dry_run):

    for file in path.iterdir():
        if file.is_file():
            organize_file(file, path, summary, dry_run)
        if file.is_dir() and file.name not in FILES_TYPE.values():
            main(file, summary, dry_run)


def print_summary(summary, dry_run):
    mode = "DRY RUN" if dry_run else "REAL RUN"
    print("\n--- Script Summary ---")
    print(f"Mode: {mode}")
    print(f"Files moved: {summary['moved_count']}")
    print(f"Files skipped: {summary['skipped_count']}")
    print(f"Files renamed: {summary['renamed_count']}")

main(args.path, summary, args.dry_run)
print_summary(summary, args.dry_run)