# File Automation Tool

A beginner-friendly Python project that automates common file and folder tasks.

## Features
- Organizes files into folders based on file extension.
- Renames files by adding a prefix entered by the user.
- Removes empty subfolders only (never deletes files).
- Uses Python's `os` module for file and folder operations.
- Handles errors with `try/except`.
- Records operations in `file_automation.log`.

## Requirements
- Python 3.x
- No external packages required.

## How to run
1. Download `file_automation.py`.
2. Open a terminal in the downloaded folder.
3. Run:

   ```bash
   python file_automation.py
   ```

4. Enter the full path of the folder you want to manage.
5. Select an operation from the menu.

**Important:** Test the program on a sample folder first. Organizing and renaming change file locations/names. Make a backup before using it on important files.

## Sample input/output

Sample folder before running:

```text
sample_files/
├── notes.txt
├── photo.jpg
└── report.pdf
```

Example session (organize by extension):

```text
===== FILE AUTOMATION TOOL =====
Enter the folder path: sample_files

Choose an operation:
1. Organize files by extension
2. Rename files with a prefix
3. Remove empty subfolders
4. Exit
Enter your choice (1-4): 1
Move files into extension folders? (y/n): y
Moved: notes.txt -> txt/
Moved: photo.jpg -> jpg/
Moved: report.pdf -> pdf/
Organization complete. 3 file(s) moved.
```

Folder after running:

```text
sample_files/
├── jpg/
│   └── photo.jpg
├── pdf/
│   └── report.pdf
└── txt/
    └── notes.txt
```

Example log entry:

```text
2026-11-11 17:00:00,000 - INFO - Moved sample_files/notes.txt to sample_files/txt/notes.txt
```

The timestamp and exact paths in your log will depend on your computer.

## GitHub upload
1. Sign in to GitHub and create a new repository named `File-Automation-Tool`.
2. Add `file_automation.py` and `README.md`.
3. Commit the files with a message such as `Add file automation script`.
4. Copy the repository URL and include it in your assignment submission.

This project folder contains the source code and README; it is not automatically published to GitHub.
