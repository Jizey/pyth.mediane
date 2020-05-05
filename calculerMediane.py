#réalisé le 14/04/2020
import os
import random
from math import *

notes = []
while True:
    nb = (input("  Ajoutez un nombre : "))
    nb = float(nb) # MAJ : inclure un Try: except / ValueError:

    notes.append(nb) #on stocke le nombre choisi dans une liste
    notes.sort() #on trie les nombres dans l'ordre croissant
    print(notes)
    med = ceil(len(notes)/2) #on détermine le nombre médian (taille du tableau divisée par 2, arrondie au supérieur)
    if len(notes) %2 == 0: #si le tableau a un nombre pair d'éléments
        print("La médiane se situe dans la liste entre les places ", med, " et ", med + 1)
        print("La valeur de la médiane est donc : ", (notes[med] + notes[med-1])/2)
    else: #si le tableau a un nombre impair d'éléments
        print("La médiane se situe dans la liste à la place ", med)
        print("La valeur de la médiane est donc : ", notes[med-1])
    continue

print("Fin du programme")

os.system("pause")