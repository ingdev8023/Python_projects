# Log Cleaner and Report Generator (Python CLI)

A Python command-line tool that cleans log files and generates a summary report.

This project reads a log file, removes empty lines and duplicate entries, preserves the original order of valid log messages, and creates both a cleaned log file and a text report with summary statistics.

## Features

- Removes empty lines
- Removes duplicate log entries
- Preserves log order
- Counts log levels (`INFO`, `WARNING`, `ERROR`)
- Generates a cleaned log file
- Generates a summary report
- CLI support with custom file path input

## Requirements

- Python 3.8+
- No external dependencies

## Usage

Run the script from the terminal:

```bash
python log_cleaner.py --path ./app.log

##How It Works

The script reads the input log file line by line.
Empty lines are skipped.
Duplicate lines are removed using a set for fast lookup.
A list is used to preserve the original order of valid log entries.
Log levels are counted from the cleaned data.
The script writes:
a cleaned log file
a summary report file

##Limitations

The script expects a plain text log file
Log level detection currently supports:
INFO
WARNING
ERROR
It does not yet support recursive processing of multiple log files


## Future Improvements

Add support for more log levels (DEBUG, CRITICAL)
Export report as CSV or JSON
Add recursive folder scanning for multiple log files
Add unit tests

## Why This Project

This project demonstrates practical skills in:

file handling
text processing
duplicate detection
report generation
CLI design

It reflects the kind of small automation tools engineers build for real operational workflows.

Author

Daniel Jaimes