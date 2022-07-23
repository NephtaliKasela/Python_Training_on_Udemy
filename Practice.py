from pickle import FALSE
import pwd
import random
import os

# id
# print(id(290))
# print(id(290))
# if (id(10000) == id(10000)):
#     print("Yes")
# true = True
# another = True
# print(id(true))
# print(id(another))

# Manipulation with characters

# print("Bonjour".upper())
# print("BONJOUR".lower())
# print("bonjour tout le monde !".capitalize())
# print("bonjour tout le monde !".title())
# print("Bonjour Bonjour".replace("jour", "soir"))
# print("   Father   ".strip())
# print("   Father   ".strip(" hre"))
# print("   Father   ".lstrip())
# print("   Father   ".rstrip())
#      # split()
# print("1, 2, 3, 4, 5")
# print("1, 2, 3, 4, 5".split(", "))
# print(", ".join("1, 2, 3, 4, 5".split(", ")))
#      # zfill()
# print("9".zfill(5))
# for i in range(5):
#     print(str(i).zfill(3))
#      # is
# if("9".isdigit):
#     print("Yes")

# Random module
# a = random.randint(0, 20)
# print(a)
# b = random.uniform(0, 20)
# print(b)
# c = random.randrange(100)
# print(c)
# d = random.randrange(0, 50, 10)
# print(d)

# os module
#chemin = r"C:\Users\NEPHTALI\OneDrive\Bureau\mainFolder"
#dossier = os.path.join(chemin, "dossier")
      # How to create a folder
# if not os.path.exists(dossier):
##      os.makedirs(dossier)
#os.makedirs(dossier, exist_ok=True) 
      # How to remove the folder
## #if os.path.exists(dossier):
##      #os.removedirs(dossier)

# list fonction
liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[0:3] # INSÉRER CODE ICI
trois_derniers = liste[-3:]# INSÉRER CODE ICI
milieu = liste[1:-1] # INSÉRER CODE ICI
premier_dernier = liste[0::5]# INSÉRER CODE ICI
print(trois_premiers)
print(trois_derniers)
print(milieu)
print(premier_dernier)

      # index
index_Martine = liste.index("Martine")
print(index_Martine)
      # sorted
sorted_list = sorted(liste)
print(sorted_list)
print(liste)
      # sort
liste.sort()
print(liste)
      # reverse
liste.reverse()
print(liste)
      # pop
element = liste.pop(-1)
print(element)
print(liste)
      # Clear
clr = liste.clear()
print(clr)
print(liste)
      # in AND not in
liste.extend([1, 2, 3, 4, 5])
liste.append(6)
if 6 in liste:
      print("True")
liste.remove(6)
if 6 not in liste:
      print("True")

      # list comprehension
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)
nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres_positifs)
nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]
print(nombres_doubles)
nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses)
