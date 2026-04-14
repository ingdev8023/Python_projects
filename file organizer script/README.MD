# File Organizer CLI (Python)

A Python CLI tool that recursively organizes files by type.

It scans a directory and its subfolders, moves files into category folders based on extension, and prevents overwriting by safely renaming duplicates.

## Features

- Recursive folder processing
- File categorization by extension
- Automatic folder creation
- Duplicate-safe renaming (e.g. file_1, file_2)
- Dry-run mode (preview changes without modifying files)
- CLI support with custom path input
- Summary report after execution

## Project Structure

.
├── organizer.py
└── README.md

## Requirements

- Python 3.8+

No external libraries required (uses standard library only).

## Usage

Run the script from the terminal:

```bash
python organizer.py

## Supported File Types

| Extension | Category  |
|----------|----------|
| .jpg     | images   |
| .png     | images   |
| .mp3     | music    |
| .mp4     | video    |
| .pdf     | documents |

## How It Works

1. The script scans the target directory recursively.
2. Each file is checked for its extension.
3. If supported, it is moved into a category folder.
4. If a file with the same name already exists, a numeric suffix is added.
5. If dry-run mode is enabled, actions are printed instead of executed.

## Author

Daniel Jaimes  
[GitHub](https://github.com/ingdev8023)