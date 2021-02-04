solution = "pendu"
affichage = ""
lettres_trouvées = ""
tour = 20

for x in solution:
    affichage = affichage + "_ "
print(affichage)

while tour != 0:

    print(affichage)
    proposition = input("Entrer proposition : ").lower()

    if proposition in solution:
        lettres_trouvées = lettres_trouvées + proposition

    else:
        tour = tour - 1
        print("Il te reste " + str(tour) + " essais !")

    affichage = ""

    for x in solution:
        if x in lettres_trouvées:
            affichage = affichage + x + " "
        else:
            affichage = affichage + "_ "
    
    if "_" not in affichage:
        break

print("Bravo, tu as gagné !")