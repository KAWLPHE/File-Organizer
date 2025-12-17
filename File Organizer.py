"""
File Organizer by Isomiddin

Description:
Automatically organizes files in a chosen directory
by their file extensions.

Example:
- Images -> images/
- Videos -> videos/
- Documents -> documents/
"""

import os
import shutil
from pathlib import Path


#Configuration

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".cpp", ".c", ".js", ".html", ".css"],
}


#Logic

def get_category(extension: str) -> str:
    """Return folder name based on file extension."""
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Other"


def organize_folder(folder_path: str) -> None:
    path = Path(folder_path)

    if not path.exists() or not path.is_dir():
        print("❌ Invalid folder path.")
        return

    files_moved = 0

    for item in path.iterdir():
        if item.is_file():
            category = get_category(item.suffix.lower())
            target_dir = path / category
            target_dir.mkdir(exist_ok=True)

            shutil.move(str(item), str(target_dir / item.name))
            files_moved += 1

    print(f"✅ Done! {files_moved} files organized.")


#UI

def main():
    print("===================================")
    print("        FILE ORGANIZER")
    print("        by Isomiddin")
    print("===================================")

    folder = input("Enter path to folder to organize: ").strip()
    organize_folder(folder)


if __name__ == "__main__":
    main()
