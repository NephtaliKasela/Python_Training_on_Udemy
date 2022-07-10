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
print("Bonjour".upper())
print("BONJOUR".lower())
print("bonjour tout le monde !".capitalize())
print("bonjour tout le monde !".title())
print("Bonjour Bonjour".replace("jour", "soir"))
print("   Father   ".strip())
print("   Father   ".strip(" hre"))
print("   Father   ".lstrip())
print("   Father   ".rstrip())
     # split()
print("1, 2, 3, 4, 5")
print("1, 2, 3, 4, 5".split(", "))
print(", ".join("1, 2, 3, 4, 5".split(", ")))
     # zfill()
print("9".zfill(5))
for i in range(5):
    print(str(i).zfill(3))
     # is
if("9".isdigit):
    print("Yes")