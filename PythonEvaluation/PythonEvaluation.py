caractere = input("Entrez un caractère :")
taille = int(input("Entrez une taille :"))

colonne = 0
ligne = 0

for ligne in range(0, taille):
    for colonne in range(0, taille, 2):
        print(caractere, end="")
        print(" ", end="")
    print("")
    if (ligne%2 == 0): 
        print(" ", end="")