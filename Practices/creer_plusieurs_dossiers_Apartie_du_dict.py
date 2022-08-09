from pathlib import Path


chemin = Path("C:/Users/NEPHTALI/OneDrive/Bureau/mainFolder/dossier")
chemin.mkdir(exist_ok=True)

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}
# Let create all main folders(Films, Employes, Exercices)
for key in d:
    # determine the path for each main folder(Films, Employes, Exercices)
    dossier = chemin / key
    # create the folder
    dossier.mkdir(exist_ok=True)
    # Let create all folders for each main folder 
    for i in range(len(d[key])):
        # determine the path for each folder
        dossier2 = dossier / d[key][i]
        # create the folder
        dossier2.mkdir(exist_ok=True)