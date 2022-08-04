employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
age_paul = 0
for key in employes:
    # increase the age
    if employes[key]["prenom"] == "Julie": 
            employes[key]["age"] += 1
            print(employes[key]["age"])
    # keep the age of "Paul" in the verable "age_paul"
    elif employes[key]["prenom"] == "Paul" : 
            age_paul = employes[key]["age"]
            print(age_paul)

# delete a key
if employes[key]["prenom"] == "Patrick": del employes[key]
# print all existant names
for key in employes:
        print(employes[key]["prenom"])