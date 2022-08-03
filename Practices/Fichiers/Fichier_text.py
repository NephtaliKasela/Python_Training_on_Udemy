chemin = r"C:\Nephterland\COURSES\PROGRAMMING\GitHub\Python_Training_on_Udemy\Practices\Fichiers\Fichier_texte.txt"
with open(chemin, "w") as f:
    f.write("Bonjour\nBonsoir\n")
with open(chemin, "a") as f:
    f.write("Bonne apres midi")
with open(chemin, "r") as f:
    content = f.read().splitlines()
    print(content)
    f.seek(0)
    content2 = f.read().splitlines()
    print(content2)
