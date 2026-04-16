#!/usr/bin/env python3

"""Log Cleaner and Report Generator (CLI Tool)

This script processes a log file, removes empty lines and duplicate entries,
writes a cleaned version to a new log file, and generates a summary report.

Features:
- Removes empty lines
- Removes duplicate log entries while preserving original order
- Counts log levels (INFO, WARNING, ERROR)
- Writes a cleaned log file
- Generates a text report with processing summary

Output files:
- <original_name>_clean.log
- <original_name>_report.txt

Usage:
    python log_cleaner.py --path ./app.log
"""



import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser(description="Review the log, cleans it and generates a report")

parser.add_argument(
    "--path",
    type=Path,
    required=True,
    help="Path to the Log file"
)

args = parser.parse_args()

def write_report(report_path, source_path, output_path, line_counter, empty_line_counter, duplicate_counter, logs_dict):
    with open(report_path, "w") as f:
        f.write("Log Cleaning Report\n")
        f.write("===================\n")
        f.write(f"Source file: {source_path.name}\n")
        f.write(f"Cleaned file: {output_path.name}\n\n")
        f.write(f"Lines processed: {line_counter}\n")
        f.write(f"Empty lines removed: {empty_line_counter}\n")
        f.write(f"Duplicate lines removed: {duplicate_counter}\n\n")
        f.write("Log levels:\n")
        for log_level, count in logs_dict.items():
            f.write(f"{log_level}: {count}\n")


def main(path):
    if not path.exists() or not path.is_file():
       print("Invalid file path")
       return

    line_counter = 0
    empty_line_counter = 0
    duplicate_counter = 0

    cleaned_lines = []
    no_duplicates = set()

    with open(path, 'r') as f:
    #removing empty lines
        for line in f:
            line_counter += 1

            if not line.strip():
                empty_line_counter += 1
                continue

            if line in no_duplicates:
                duplicate_counter += 1
                continue

            no_duplicates.add(line)
            cleaned_lines.append(line)

    # write to new file
    output_path = path.with_name(path.stem + "_clean.log")
    #report file
    report_path = path.with_name(path.stem + "_report.txt")

    #writing in the new file    
    with open(output_path, 'w') as f:
        f.writelines(cleaned_lines)   

    #processing logs
    logs_dict = {}
    
    pattern = r'(ERROR|INFO|WARNING)'
    for i in cleaned_lines:
        match = re.search(pattern, i)
        if match:
            if not match.group(0) in logs_dict:
                logs_dict[match.group(0)] = 0
            logs_dict[match.group(0)] += 1

    write_report(report_path, path, output_path, line_counter, empty_line_counter, duplicate_counter, logs_dict)

main(args.path)