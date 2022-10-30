wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
    print("Witamy!")
   

imie = input("Podaj Imię: ")
print ("Czesc", imie)


plec = input("Podaj swoją płeć (M/K)")
plec = str(plec)
if plec == "M":
	print ("jestes menem")
if plec == "K":
	print ("jestes kobieta")
else:
    print("Błędne dane, wprowadz ponownie, błędne dane")






