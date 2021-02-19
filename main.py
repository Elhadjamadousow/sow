# EXO3
def liste(num = [2,4,7,8,2], nume = [1,3,9,4,6,7]):
    liste = []
    for i in num:
        if i not in nume:
            if i not in liste:
                liste.append(i)
    for i in nume:
        if i not in num:
            if i not in liste:
                liste.append(i)
    return liste
r = liste()
print(r,"resultat exo3")
# EXO2
def mots(mo = "saliou", mot = "mamadou" ):
    nouvo = []
    for i in mo:
        for j in mot:
            if i == j:
                if i not in nouvo:
                    nouvo.append(i)
    print(nouvo,"resultat exo2")
    return nouvo
mots()

# EXO1
def tableau():
    tab = [1,2,3,4,5]
    tab.reverse()
    print(tab," resulta exo1")
tableau()
