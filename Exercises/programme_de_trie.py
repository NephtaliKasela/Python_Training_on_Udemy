from pathlib import Path

# create the dictionary
Dirs = {".png": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Archives",
        ".zip": "Documents",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".json": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"}

# determine the path where we want to make order
tri_dir = Path.home() / "Downloads"
# create the main folder
tri_dir.mkdir(exist_ok=True)
# collecte all files in the main folder
files = [file for file in tri_dir.iterdir() if file.is_file]
# Let sort them
for f in files:
    # determine the path where we want to store the file
    output_dir = tri_dir / Dirs.get(f.suffix, "Autres")
    # create the specific folder
    output_dir.mkdir(exist_ok=True)
    # move the file from the main folder to the specific folder
    f.rename(output_dir / f.name)