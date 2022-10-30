wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
    print("Witamy!")

płeć = input("podaj płeć: 'M' lub 'F': ")
M = 'M'
F = 'F'
if płeć == F:
    print("Aperol gratis")
else:
    print('przejdź do kasy')
