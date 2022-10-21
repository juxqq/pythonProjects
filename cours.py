################
# LIST
################

# faire une copie d'une liste
laliste2 = [100, 50, 65, 82, 23]
laliste2c = laliste2.copy()
print(laliste2c)

# faire une "jointure" de liste
liste1 = ["x", "y", "z"]
liste2 = [1, 2, 3]
liste3 = liste1 + liste2
print(liste3)

# autre méthode
liste1 = ["x", "y", "z"]
liste2 = [1, 2, 3]

for x in liste2:
        liste1.append()
print(liste1)

# et encore une autre méthode
liste1 = ["x", "y", "z"]
liste2 = [1, 2, 3]

liste1.extend(liste2)
print(liste1)

# clear() va vider la liste
liste1 = ["x", "y", "z"]
list1.clear()
print(liste1)

################
# LES TUPLES
################

montuple = ("Pomme","Kiwi", "Citron")
print(montuple)
print(type(montuple))
print(len(montuple))

# créer un tuple avec un objet
montuple = ("poire",)
print(type(montuple))

# et ici ?
montuple = ("poire")
print(type(montuple))

#On peut mélanger les types et avoir des tuples constitués de booléens, de chaînes, d'entier etc..
#Le tuple est une classe comme les autres types en python
#Faire appel au constructeur du tuple

montuple = tuple(("pomme", "poire", "kiwi"))
print(montuple)
print(montuple[1]) #me retourne l'élément poire
print(montuple[-1]) #me retourne le dernier élément

# me retourne poire... pas de surprise !

montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
print(montuple[2:5])

# on accède du coup à l'élément 3,4 et 5 (en position) mais pas 6

montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
print(montuple[:4])
# me donne les 4 premiers éléments de mon tuple

montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
print(montuple[2:])
# me donne le troisième élément en position inclut jusqu'à la fin du tuple

montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
print(montuple[-4:-1])
# on a pas le dernier élément puis on aura Melon, Fraise et Banane

montuple = ("Pomme", "Kiwi", "Citron", "Banane", "Fraise", "Melon", "Cerise")
if "Citron" in montuple:
        print("Oui Citron y est...")

# Comment mettre à jour un élément de mon tuple... pourtant il est immuable ?

montuple = ("Pomme", "Kiwi", "Citron")
a.list(montuple)
a[1] = "fraise"
montuple = tuple(a)

montuple = ("Pomme", "Kiwi", "Citron")
a = list(montuple)
a.append("Pastèque")
montuple = tuple(a)
print(montuple)

# Ajouter un tuple à un tuple
montuple = ("Pomme", "Kiwi", "Citron")
a = ("Fraise",)
montuple += a
print(montuple)

# Supprimer un élément
montuple = ("Pomme", "Kiwi", "Citron")
a=list(montuple)
a.remove("Pomme")
montuple = tuple(a)
print(montuple)

# Supprimer le tuple en entier
montuple = ("Pomme", "Kiwi", "Citron")
del montuple
print(montuple)

# Récupérer les éléments du tuple dans des variables
montuple = ("Pomme", "Kiwi", "Citron")
(a, b, c) = montuple
print(a)
print(b)
print(c)

# Récupérer les éléments du tuple dans des variables
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
(a, b, *c) = montuple
print(a)
print(b)
print(c)

# Parcourir un tuple via une boucle
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
for x in montuple:
    print(x)

# Parcourir un tuple en utilisant le numéro d'index et la longueur du tuple
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
for x in range(len(montuple)):
    print(montuple[x])

# Et avec un while
montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")
x = 0
while x < len(montuple):
    print(montuple[x])
    x = x + 1

# Joindre des tuples et les multiplier
montuple1 = ("Pomme", "Kiwi", "Citron")
montuple2 = (4, 12, 6)
montuple3 = montuple1 + montuple2
print(montuple3)
montuple4 = montuple1 ** 2
print(montuple4)

# Pour importer un fichier python dans un autre, par exemple dans main.py je veux importer code.py

import code

# =============

import importlib
file  = importlib.import_module("Code")
obj = file.Codeclass()
obj.show()

# =============

from Code import CodeClass
var1 = CodeClass()
var1.show()
