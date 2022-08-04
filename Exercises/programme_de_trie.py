from pathlib import Path


films = {"Le Seigneur des Anneaux": 12,
        "Harry Potter": 9,
        "Blade Runner": 7.5}
prix = 0
for i in range(3):
    if i == 0:
        prix += films.get("Le Seigneur des Anneaux", 0)
    if i == 1:
        prix += films.get("Harry Potter", 0)
    if i == 2:
        prix += films.get("Blade Runner", 0)
print(prix)

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

tri_dir = Path.home() / "Downloads"
tri_dir.mkdir(exist_ok=True)
files = [file for file in tri_dir.iterdir() if file.is_file]
for f in files:
    output_dir = tri_dir / Dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)