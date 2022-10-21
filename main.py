
# exo 1
prenom = "Pierre"
age = 20
majeur = True
compte_en_banque = 0
# j'ai eu un crash internet sur celui-ci quand je suis revenu l'exercice n'y était plus malheureusement...

# exo 2
nombre = 15
print('le nombre est', str(nombre))

# exo 3
a = 2
b = 6
c = 3
print(f"{a} + {b} + {c}")
print(a, b, c, sep=" + ")

# exo 4
list1 = range(3)
list2 = range(5)

print(list(list1))
print(list(list2))

# exo 5
prenom = "Pierre"
if type(prenom) == str:
    print("La variable est une chaîne de caractères")
else:
    print("La variable n'est pas une chaîne de caractères")
prenom = 0;
if type(prenom) == str:
    print("La variable est une chaîne de caractères")
else:
    print("La variable n'est pas une chaîne de caractères")


def checkIfItemIsString(item):
        if isinstance(item, str):
            print(item + " is a string.")

firstName = 'Pierre';
checkIfItemIsString(firstName);
firstName = 0;
checkIfItemIsString(firstName);

# exo 6
phrase = "Bonjour tout le monde, Bonjour encore !"
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir", 1)
print(nouvelle_phrase)

# exo 7
chaine = "Pierre, Julien, Anne, Marie, Lucien"
newChaine = chaine.split(", ")
print(sorted(newChaine))


names = "Pierre, Julien, Anne, Marie, Lucien"
namesArray = names.split(', ')
namesArray.sort()
print(", ".join(map(str,namesArray)))

# exo 8
from math import pi

rayon = 10
volume = ((4 * pi / 3)) * rayon**3
print("Le volume de la sphère est", volume)

import math;
def calculateRadius(radius: float) :
    return ((4*math.pi)/3) * radius**3;
print(calculateRadius(10));

# exo 9
def checkIfGreaterThanTen(number):
    if isinstance(number, int):
        if number > 10:
            print(str(number) + " est plus grand que 10.")
        if number == 10:
            print(str(number) + " est égal à 10.")
        else:
            print(str(number) + " est plus petit que 10.")
    else:
        print(str(number) + " n'est pas un nombre.")
print("Entrez un nombre : ")
inputNumber = input()
checkIfGreaterThanTen(int(inputNumber))

# exo 10
def createList(number1, number2):
    listNumber = []
    while number1 < number2:
        listNumber.append(number1)
        number1 += 1
    return listNumber
a = 5
b = 15
print(createList(a, b))


