print("==== Ma calculatrice ====")
#Saisie des nombres
while True:
     nombre1 = float(input("entrez le premier nombre :"))
     operateur = input("choisissez une operation (+,-,*,/) : ")
     nombre2 = float(input("entrez le deuxieme nombrre : "))
     #Calcul
     if operateur == "+":
          resultat = nombre1 + nombre2

     elif operateur == "-":
          resultat = nombre1 - nombre2

     elif operateur == "*":
          resultat = nombre1 * nombre2

     elif operateur == "/":
          if nombre2 != 0:
               resultat = nombre1 / nombre2
          else:
               resultat = "Ereur : division par zero"
     else:
          resultat = " Operation invalide"

     # Affichage du resultat     
     print("RESULTAT EST :", resultat)

     continuer = input ("voulez-vous continuer ? ( oui \ non) : ")

     if continuer.lower() == "oui":
          print("Nouveau calcul !")
     else:     
          print("MERCI D'AVOIR UTILISER MA CALCULATRICE!!!")
          break           



      


