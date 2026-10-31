# Automated Backup Tool

A Python-based command-line application that makes it easy to create, manage, and restore file backups.

## Features

- Automatic backups: Copy files from a selected source folder.
- Timestamped backups: Every backup is saved in a separate folder with a unique timestamp.
- Folder structure preservation: Maintains the original directory structure.
- File restoration: Restore files from a previously created backup.
- Backup reports: Displays the number of successfully copied and failed files.
- Error handling: Reports files that could not be copied or restored.
- Folder validation: Prevents source and destination folders from being nested inside each other.

## Technologies Used

- Python
- pathlib
- shutil
- datetime

## Requirements

- Python 3 installed
- Windows, macOS, or linux
- Terminal or command prompt

## How to Run

1. Clone or download this repository.
2. Open a terminal inside the project directory and run:
		python backup.py 

## How to Use 

When you run the application, you will see three options:

1. Create a new backup.
2. Restore files from a backup.
3. Exit

Follow the prompts to provide the required folder paths.

## Learning Objectives

This project demonstrates practical Python programming concepts, including:

- Functions
- Loops and conditional statements
- Exception handling
- File and directory management
- Working with dates and timestamps
- Using Python standard library modules

## Future Improvements

- Scheduled automatic backups
- Incremental backups
- Backup compression
- Graphic User Interface