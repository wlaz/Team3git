wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
    print("Witamy!")

# Specjalne ceny dla osób 40+

if wiek >= 40:
    print("Mamy dla Ciebie specjalne ceny!")
else:
    print("Zapraszam do kasy")
