import random


#Exercise : Jeu de role 
'''Règles du jeu
Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.
Le jeu comporte deux joueurs : vous et un ennemi.
Vous commencez tous les deux avec 50 points de vie.
Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
L'ennemi ne dispose d'aucune potion.
Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
Lorsque vous utilisez une potion, vous passez le prochain tour.'''

print("\n=== Que le meilleur gagne ===\n")
point_joueur = 50
point_enemi = 100         
count = 0
nombre_de_coup = 0
while point_joueur > 0 or point_enemi > 0:
    choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    
    # Verifier si le nombre entré par l'utilisateur est bel est bien un nombre intier 
    try:
        choice = int(choice)
        if choice == 1:
            nombre_de_coup += 1
            attaque_du_joueur = random.randint(5, 10)
            attaque_de_enemi = random.randint(5, 15)
            point_enemi -= attaque_du_joueur
            point_joueur -= attaque_de_enemi

            #Afficher le score
            print(f"Vous avez infligé {attaque_du_joueur} point(s) de dégas à l'enemi.")
            print(f"L'enemi vous a infligé {attaque_de_enemi} point(s) de dégas.")
            if point_enemi > 0 and point_joueur > 0:
                print(f"Il vous reste {point_joueur} point(s) de vie.")
                print(f"Il reste {point_enemi} point(s) de vie à l'enemi.")
                print("-"*50)
            else:
                # Afficher le resultat final
                print("Fin de la partie...")
                point_joueur += attaque_de_enemi
                point_enemi += attaque_du_joueur 
                if point_enemi > point_joueur:
                    print("Vous avez perdu.")
                elif point_joueur > point_enemi:
                    print("Vous avez gagné.")
                else:
                    print("Vous êtes à égalité.")
                print(f"La partie est fini en {nombre_de_coup} manche(s).")
                break
        # ajouter les points au joueur
        if choice == 2:
            if count < 3:
                potion = random.randint(15, 50)
                point_joueur += potion
                print(f"Votre point est de {point_joueur}")
            else:
                print("Votre potion est fini...")
            count += 1
    except:
        choice = -1    

i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        continue
