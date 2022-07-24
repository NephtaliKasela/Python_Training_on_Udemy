# exercise : log in
mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
count = 0

if mdp == "":
    print(mdp_trop_court.upper())
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
else:
    if len(mdp) >= 8:
        flag = False
        while count < len(mdp):
            try:
                mdpsecond = int(mdp[count])
            except:
                flag = True
                break
            count += 1
        if flag == False:
            print("Votre mot de passe ne contient que des nombres.")
        else:
            print("Inscription terminée.")
