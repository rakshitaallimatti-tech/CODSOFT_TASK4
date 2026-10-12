import os

os.makedirs("my_files", exist_ok=True)

with open("my_files/sample.txt", "w") as f:
    f.write("This is my backup test file.")

print("my_files folder created!")
print("Test file created!")
import os
import shutil
from datetime import datetime

SOURCE = "my_files"
BACKUP = "backups"

os.makedirs(SOURCE, exist_ok=True)
os.makedirs(BACKUP, exist_ok=True)

def create_backup():
    files = os.listdir(SOURCE)

    if not files:
        print("my_files folder is empty!")
        print("Add a file to my_files and try again.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(BACKUP, "backup_" + timestamp)

    shutil.copytree(SOURCE, backup_folder)
    print("Backup successful!")
    print("Saved at:", backup_folder)

def show_backups():
    items = sorted(os.listdir(BACKUP), reverse=True)

    if not items:
        print("No backups found.")
        return []

    for i, item in enumerate(items, 1):
        print(i, item)

    return items

def restore_backup():
    items = show_backups()

    if not items:
        return

    try:
        choice = int(input("Choose backup number: "))
        if choice < 1 or choice > len(items):
            print("Invalid choice!")
            return

        source = os.path.join(BACKUP, items[choice - 1])

        # Restore into a separate folder to protect current files
        destination = "restored_files"
        if os.path.exists(destination):
            shutil.rmtree(destination)

        shutil.copytree(source, destination)
        print("Restore successful!")
        print("Restored files are in:", destination)

    except ValueError:
        print("Enter a valid number.")

while True:
    print("\n=== CLOUD BACKUP & RESTORE SYSTEM ===")
    print("1. Create backup")
    print("2. View backup history")
    print("3. Restore a backup")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        create_backup()
    elif choice == "2":
        show_backups()
    elif choice == "3":
        restore_backup()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
        
        

