# Exercise : liste de courses
menu = '''-- Faites votre choix -- 
1. Ajouter un élément à la liste de courses
2. Retirer un élément de la liste de courses
3. Afficher les éléments de la liste de courses
4. Vider la liste de courses
5. Quitter le programme
'''
choice = -1
count = 1
liste_de_courses = []
while True:
    print(menu)
    choice = input("Entrer votre choix : ")
    try:
        choice = int(choice)
        # Ajouter un element
        if choice == 1:
            element = input("Entrer un element: ")
            liste_de_courses.append(element)
            print(f"L'element >> {element} << à été ajouté")
            count += 1
        # Supprimer un element
        elif choice == 2:
            element = input("Quel element ? ")
            flag = False
            for i in liste_de_courses:
                if i == element:
                    liste_de_courses.remove(element)
                    print(f"L'element >> {element} << a été supprimé")
                    flag = True
                    count -= 1

            if flag == False:
                    print(f"L'element >> {element} << n'existe pas dans la liste...")
        # Afficher les elements           
        elif choice == 3:
            print("Voici votre liste :")
            if count != 0:
                index = 1
                for i in liste_de_courses:
                    print(f"{index}. {i}")
                    index += 1
            else:
                print("Aucun élement")
        # Affacer tous les elements de la liste
        elif choice == 4:
            if count == 1:
                print("La liste est déjà vide...")
            else:
                liste_de_courses.clear()
                print("Tous les element ont été éffacés...")
            count = 1
        # Quitter la partie
        elif choice == 5:
            break
        # Signaler à l'utilisateur que le nombre doit etre compris entre 1 et 5
        else:
            print("Entrez un nombre entre 1 et 5")
    except:                
        print("Veillez entrer un nombre...")
    print("---------------------------------")