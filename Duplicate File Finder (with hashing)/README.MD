# Duplicate File Finder (Python CLI)

A Python command-line tool to detect duplicate files based on content.

This tool scans a directory, groups files by size, and then uses hashing (MD5) to confirm duplicates efficiently.

## Features

- Detects duplicate files based on content (not just file name)
- Efficient approach using size pre-filtering before hashing
- Uses modern Python hashing (`hashlib.file_digest`)
- CLI support with custom path input
- Clean and readable output

## Requirements

- Python 3.11+ (required for `hashlib.file_digest`)
- No external dependencies

## Usage

Run the script from the terminal:

```bash
python duplicate_finder.py

python duplicate_finder.py --path ./your-folder


---

## 🔹 Example Output

```md
## Example Output

Duplicate files found:

Hash: 5d41402abc4b2a76b9719d911017c592

- downloads/photo1.jpg
- downloads/photo_copy.jpg

## How It Works

1. The script scans the target directory.
2. Files are grouped by extension and size.
3. Only groups with matching extension and sizes are hashed.
4. Files with identical hashes are considered duplicates.

## Limitations

- Only processes files in the specified directory (non-recursive)
- Does not delete or move duplicates (read-only tool)
- Uses MD5 (sufficient for duplicate detection but not for security purposes)

## Future Improvements

- Add recursive directory scanning
- Add option to delete or move duplicates
- Add dry-run mode for safe operations
- Add summary report with counts
- Support for other hashing algorithms (SHA-256)

## Why This Project

This project demonstrates practical file system handling, efficient data processing, and the use of hashing for real-world problem solving.

## Author

Daniel Jaimes  
[GitHub](https://github.com/ingdev8023)