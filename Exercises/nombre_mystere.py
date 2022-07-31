# Exercise : nombre mystère
import random


print("\n=== Le nombre mystère ===\n")
nombre_random = random.randint(0, 5)
counter = 1
count = 5
while count != 0:
    sentence = "Vous avez 5 essaies." if count == 5 else f"il vous reste {count} essaies"
    sentence2 = "il vous reste 1 essaie"
    # Afficher le nombre d'essaies qui restent
    if count == 1:
        print(sentence2)
    else:
        print(sentence)
    # Demander l'utilisareur d'entrer un nombre
    nombre = input("Devine le nombre : ")
    try:
        # Comparer si le nombre entré par l'utilisateur est égale au nombre mystère
        flag = False
        nombre = int(nombre)
        if nombre == nombre_random:
            print(">> Great <<")
            print(f"Vous avez trouvé le nombre à l'éssaie {counter}.")
            flag = True
            break
        else:
            print("Faux. Essaies encore...")
        count -= 1
        counter += 1
    
    except:             # Avertir si l'utilisateur entre autre chose qu'un nombre
        print("Veillez entrer un nombre...")

# Donner la reponse en cas d'échec 
if flag == False:
    print(f"Dommage ! Le nombre était {nombre_random}")