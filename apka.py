wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
   	print("Witamy!") 
elif wiek < 18:
	print ("Zgoda od rodziców")


    
