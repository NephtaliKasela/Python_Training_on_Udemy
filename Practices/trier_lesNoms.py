from pathlib import Path


# determine the path of the file where we want to get data
chemin = Path("C:/Users/NEPHTALI/OneDrive/Bureau/mainFolder/prenoms.txt")
# create the file if it does not exist
chemin.touch(exist_ok=True)
# read all data form the file
with open(chemin, "r") as f:
    premons = f.readlines()
# split them and put them in a list
premons = premons[0].split()
print("Before:\n", premons)
# remove all ponctuations and put all names in another list
all_names = [prenom.strip(" .,") for prenom in premons]
# sort the list and print them
all_names.sort()
print("\nAfter:\n")
for name in all_names:  print(name)