# Construire un code qui affiche une liste des nombres pairs de 1 à 100
liste_nombres_pairs = range(2, 101, 2)
print(list(liste_nombres_pairs))

# Construire un code qui affiche le lancé de 6 dés aléatoires
import random

for x in range(6):
    nombre = random.choice(range(1,7))
    print(nombre)

# Construire un code qui génère un nombre de lancé de dés choisi par l'utilisateur et afficher la moyenne en flottant de l'ensemble de ces lancés
import random

y = int(input())
listNumber = []
for x in range(y):
    nombre = random.choice(range(1,7))
    listNumber.append(nombre)
    moyenne = sum(listNumber) / len(listNumber)
print(moyenne)

# Compter le nombre d'occurence d'une lettre dans une phrase, par exemple "Salut ça va?" compter le nombre de a soit 3
lettre = "a"
phrase = "Salut ça va?"
print(phrase.lower().count(lettre))

# EXTENSION BASIQUE : pensez au cas de figure ou la lettre est en majuscule...
# EXTENSION : Compter le nombre d'occurence de chaque lettre puis afficher la fréquence de chaque lettre de la phrase

phrase = "Salut ça va ?"
for lettre in phrase:
    print("Lettre : ", lettre, " Nombre d'occurence(s) : ", phrase.count(lettre))