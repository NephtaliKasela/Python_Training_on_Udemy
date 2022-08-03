import json

chemin = r"C:\Nephterland\COURSES\PROGRAMMING\GitHub\Python_Training_on_Udemy\Practices\Fichier_Json.json"
with open(chemin, "r") as f:
    # json.dump('''list(range(10))
    # bonjour
    # bonsoir''', f, indent=4)
    content = json.load(f)
    print(content)
      