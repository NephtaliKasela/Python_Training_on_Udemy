# Exercise : Check if the file is a python file
from pathlib import Path


# get data from the user
chemin = Path(input("Entrer le chemin: "))
# collect all files from the folder and put them in the list 
chemin_contenant_tousLes_fichiers = Path("C:/Users/NEPHTALI/OneDrive/Bureau/mainFolder/Verification_fichiers")
files = [file for file in chemin_contenant_tousLes_fichiers.iterdir() if file.is_file]
# Check if the file entered by the user is in the list of files  
isnotFile = False
for file in files:
    try:
        # Compare the file entered by the user with the file in the list
        if chemin.name == file.name:
            if file.suffix == ".py":    # print a message if the file is a python file
                print("C'est bien un fichier Python.")
            elif chemin.suffix == ".txt":      # Read the file if that file is a text file
                with open(chemin, "r") as f:
                    read = f.read()
                    print(read)
            else:       # print a message if the file is not a python file and not a text file
                print(f"Votre chemin contient l'extension {chemin.suffix} \nCe n'est pas un fichier Python.")
        else:     
            isnotFile = True
    # print a message if the file is not found
    except:
        print(f"{chemin} n'est pas un fichier.")
if isnotFile: print("Fichier introuvable...")


# fichier = input("Entrez un fichier à ouvrir : ")

# try:
#     f = open(fichier, "r")
#     print(f.read())
# except FileNotFoundError:
#     print("Le fichier est introuvable.")
# except UnicodeDecodeError:
#     print("Impossible d'ouvrir le fichier.")
# else:
#     f.close()