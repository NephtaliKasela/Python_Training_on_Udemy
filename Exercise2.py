# exercise : addition
a = ""
b = ""
while True:
    a = input("Entrez un premier nombre  : ")
    b = input("Entrez un deuxième nombre : ")
    try:
        a = int(a)
        b = int(b)
        print(f"Le résultat de l'addition de {a} avec {b} est égal à {a + b}")
        break
    except:
        print("Veuillez entrer deux nombres valides")
        continue