import shutil
from pathlib import Path
from datetime import datetime

def create_backup(source_folder , backup_folder):
    source = Path(source_folder).resolve()
    destination = Path(backup_folder).resolve()
    
    if not source.is_dir():
        print("Error: Source folder does not exist.")
        return
        
    if ( destination == source or source in destination.parents or destination in source.parents):
        print("Error: Source and backup folders cannot be inside each other.")
        return
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    destination = destination / f"backup_{timestamp}"
    
    destination.mkdir(parents=True, exist_ok=True)
    
    copied_files = 0
    failed_files = 0
    
    
    
    print("\nStarting backup...")
    
    for file_path in source.rglob("*"):
        if file_path.is_file():
            try:
                relative_path = file_path.relative_to(source)
                destination_path = destination / relative_path
                destination_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, destination_path)
                
                copied_files += 1
                
                print(f"Copied: {relative_path}")
            except OSError as error:
                failed_files += 1
                print(f"Could not copy {file_path}: {error}")
    print("\n============================================================================ BACKUP REPORT =====================================================================================================")
    
    print(f"Files copied successfully: {copied_files}")
    
    print(f"Files failed: {failed_files}")
    
    print(f"Backup location: {destination}")
    
    if failed_files == 0:
        print("Backup completed successfully!")
    else:
        print("Backup completed with some errors.")
    
    
print("======================================================================================================================================================================================================")

def main():

    while True:

        print("\n================================")
        print("       AUTOMATED BACKUP TOOL")
        print("================================")
        print("1. Create a new backup")
        print("2. Restore files from a backup")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":

            source_folder = input(
                "Enter the source folder path: "
            ).strip()

            backup_folder = input(
                "Enter the backup destination path: "
            ).strip()

            create_backup(source_folder, backup_folder)

        elif choice == "2":

            backup_folder = input(
                "Enter the backup folder path: "
            ).strip()

            restore_folder = input(
                "Enter the restore destination path: "
            ).strip()

            restore_backup(backup_folder, restore_folder)

        elif choice == "3":

            print("\nThank you for using Automated Backup Tool!")
            break

        else:

            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()