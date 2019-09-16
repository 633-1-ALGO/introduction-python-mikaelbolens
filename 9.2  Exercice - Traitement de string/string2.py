# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

cpt = 0
nouvellePhrase = ""
i = 0


phrase = texte.split()

while i < phrase.__len__():
     if "exemple" in phrase[i] :
         cpt += 1
     if "est" in phrase[i] :
        phrase[i] = "représente"
     i += 1
i = 0

while i < phrase.__len__():
    nouvellePhrase += phrase[i] + " "
    i += 1


print("nombre d'occurence : ", cpt)
print(nouvellePhrase)



