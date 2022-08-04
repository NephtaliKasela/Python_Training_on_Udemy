import shutil
from pathlib import Path


p = Path("c:/Nephterland/COURSES/PROGRAMMING/GitHub/Python_Training_on_Udemy/Practices")
p = p / "module_Path.py"
# Quelques options utiles
print(p.home())
print(p.parent)
print(p.parent.parent.parent)
print(p.cwd())
print(p.name)
print(p.suffix)
print(p.suffixes)
print(p.stem)
print(p.exists())
print(p.is_dir())
print(p.is_file())

chemin = Path("C:/Users/NEPHTALI/OneDrive/Bureau/mainFolder")
# concatenation de dossiers 
chemin = chemin / "Ndossier"
chemin.mkdir(exist_ok = True)
chemin = chemin / "1" / "2" / "3"
chemin.mkdir(parents=True, exist_ok=True)

# concatenation avec un fichier
chemin = chemin / "readme.txt"
# ajouter un ficher text
chemin.touch()
chemin.write_text("bonjour")
# supprimer un ficher text
chemin.unlink()

# supprimer un dossier qui ne contient rien
chemin = chemin.parent
print(chemin)
chemin.rmdir()
print(chemin)
chemin = chemin.parent.parent
print(chemin)

# supprimer un dossier qui contient d'autres dossiers
shutil.rmtree(chemin)
print(chemin)

# rechercher un ficher dans un dossier
chemin = Path.home() / "Downloads"
for f in chemin.glob("*.mp4"):         # ou utiliser "rglob" a la place de "glob" pour plus d'informations
    print(f.name)                    

# rechercher un ficher ou un dossier
liste = [i for i in chemin.iterdir() if i.is_file()]
for i in liste: print(i.name)
print(liste[2].stem)
