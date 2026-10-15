# Python Log Analyzer

A simple Python project that reads a log file, counts INFO / WARNING / ERROR messages, and saves a report.

## Features

- Reads log data from sample.log
- Counts log levels (INFO, WARNING, ERROR)
- Shows the most frequent errors
- Saves the result in report.txt
- Shows a warning if too many errors are found
- Handles missing log file without crashing

## Project Structure

log_analyzer/
├── analyzer.py
├── sample.log
├── report.txt
└── README.md
## How to Run

python analyzer.py
## Sample Output

===== LOG REPORT =====
Total lines: 8

Level count:
  INFO: 3
  WARNING: 2
  ERROR: 3

Top errors:
  Database connection failed -> 2 times
  Timeout while loading page -> 1 times
## Technologies

- Python 3
- File Handling
- collections.Counter
- datetime

## Author

RazinHossainSagor