import os
import shutil

# Base path
path = r"D:\files"

# File type dictionary
file_types = {
    "Image": ['jpg', 'png', 'jpeg', 'bmp', 'svg', 'gif'],
    "Excel": ['csv', 'xls', 'xlsx'],
    "Zip":   ['zip', 'rar', '7z'],
    "Text":  ['txt', 'md', 'log'],
    "PDF":   ['pdf'],
    "Word":  ['doc', 'docx'],
    "PowerPoint": ['ppt', 'pptx'],
    "Video": ['mp4', 'mkv', 'avi', 'mov'],
    "Audio": ['mp3', 'wav', 'flac'],
    "Code":  ['py', 'java', 'cpp', 'c', 'js', 'html', 'css']
}

# Sample files for testing
sample_files = [
    "image1.jpg", "photo.png", "pic.jpeg",
    "notes.txt", "readme.txt",
    "data.csv", "report.xlsx",
    "archive.zip", "ebook.pdf",
    "assignment.docx", "presentation.pptx",
    "video.mp4", "song.mp3",
    "script.py", "index.html"
]


def organize_files():
    """Move files into their respective folders."""
    if not os.path.exists(path):
        print(f"{path} does not exist!")
        return

    # Create category folders
    for folder in file_types.keys():
        os.makedirs(os.path.join(path, folder), exist_ok=True)

    # Move files
    for file in os.listdir(path):
        filepath = os.path.join(path, file)

        if os.path.isdir(filepath):
            continue

        _, ext = os.path.splitext(file)
        ext = ext.lower().lstrip('.')

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                shutil.move(filepath, os.path.join(path, folder, file))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(other_folder, file))

    print("Files have been organized.")


def truncate_folder():
    """Delete everything inside the folder."""
    if not os.path.exists(path):
        return

    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)

    print("Folder has been emptied.")


def create_sample_files():
    """Create sample test files."""
    os.makedirs(path, exist_ok=True)

    for file in sample_files:
        file_path = os.path.join(path, file)
        open(file_path, "a").close()  # empty placeholder files

    print(f"Sample files created in {path}")


if __name__ == "__main__":
    # Example usage
    # unncomment and use any functionality you want for starters you may create some sample files
    # then organise them into subfolders and then try truncating them 

    truncate_folder()
    # create_sample_files()
    # organize_files()
