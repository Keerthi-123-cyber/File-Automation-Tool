import os
import logging

# Create a log file to record all operations
logging.basicConfig(
    filename="file_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_directory():
    """Ask the user for the folder to work on and validate it."""
    folder = input("Enter the folder path: ").strip().strip('"')
    if not os.path.isdir(folder):
        print("Error: The folder does not exist.")
        logging.error("Invalid directory entered: %s", folder)
        return None
    return folder

def organize_files(folder):
    """Move files into folders based on their file extensions."""
    moved = 0
    try:
        for name in os.listdir(folder):
            source = os.path.join(folder, name)
            if not os.path.isfile(source):
                continue

            extension = os.path.splitext(name)[1].lower().lstrip(".")
            folder_name = extension if extension else "no_extension"
            destination_folder = os.path.join(folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(destination_folder, name)
            if os.path.exists(destination):
                print(f"Skipped (already exists): {name}")
                logging.warning("Skipped existing destination: %s", destination)
                continue

            os.rename(source, destination)
            moved += 1
            print(f"Moved: {name} -> {folder_name}/")
            logging.info("Moved %s to %s", source, destination)

        print(f"Organization complete. {moved} file(s) moved.")
    except OSError as error:
        print(f"File operation error: {error}")
        logging.exception("Error while organizing files")

def rename_files(folder):
    """Add a user-provided prefix to files in the selected folder."""
    prefix = input("Enter a prefix to add to filenames: ").strip()
    if not prefix:
        print("Prefix cannot be empty.")
        return

    renamed = 0
    try:
        for name in os.listdir(folder):
            source = os.path.join(folder, name)
            if not os.path.isfile(source):
                continue

            new_name = prefix + name
            destination = os.path.join(folder, new_name)

            if os.path.exists(destination):
                print(f"Skipped (name already exists): {new_name}")
                logging.warning("Rename skipped; destination exists: %s", destination)
                continue

            os.rename(source, destination)
            renamed += 1
            print(f"Renamed: {name} -> {new_name}")
            logging.info("Renamed %s to %s", source, destination)

        print(f"Renaming complete. {renamed} file(s) renamed.")
    except OSError as error:
        print(f"File operation error: {error}")
        logging.exception("Error while renaming files")

def clean_empty_folders(folder):
    """Remove empty subfolders (does not delete files)."""
    removed = 0
    try:
        # Walk bottom-up so nested empty folders can also be removed.
        for current, directories, _ in os.walk(folder, topdown=False):
            for directory in directories:
                path = os.path.join(current, directory)
                try:
                    os.rmdir(path)  # Removes only empty directories
                    removed += 1
                    print(f"Removed empty folder: {path}")
                    logging.info("Removed empty directory: %s", path)
                except OSError:
                    # Non-empty folders are intentionally left untouched.
                    pass
        print(f"Cleaning complete. {removed} empty folder(s) removed.")
    except OSError as error:
        print(f"Folder cleaning error: {error}")
        logging.exception("Error while cleaning empty folders")

def main():
    print("\n===== FILE AUTOMATION TOOL =====")
    folder = get_directory()
    if folder is None:
        return

    while True:
        print("\nChoose an operation:")
        print("1. Organize files by extension")
        print("2. Rename files with a prefix")
        print("3. Remove empty subfolders")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            confirm = input("Move files into extension folders? (y/n): ").strip().lower()
            if confirm == "y":
                organize_files(folder)
            else:
                print("Operation cancelled.")
        elif choice == "2":
            rename_files(folder)
        elif choice == "3":
            confirm = input("Remove empty subfolders only? (y/n): ").strip().lower()
            if confirm == "y":
                clean_empty_folders(folder)
            else:
                print("Operation cancelled.")
        elif choice == "4":
            print("Thank you for using File Automation Tool!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        logging.warning("Program interrupted by user")
    except Exception:
        print("An unexpected error occurred. Check file_automation.log.")
        logging.exception("Unexpected application error")
