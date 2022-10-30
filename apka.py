wiek = input("Podaj wiek: ")

# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
   	print("Witamy!") 
elif wiek < 18:
	print ("Zgoda od rodziców")

płeć = input("podaj płeć: 'M' lub 'F': ")
if płeć == 'F':
    print("Aperol gratis")
else:
    print('przejdź do kasy i kup sobie Panie')

# Specjalne ceny dla osób 40+

if wiek >= 40:
    print("Mamy dla Ciebie specjalne ceny!")
else:
    print("Zapraszam do kasy")
region = input("Podaj region EUR lub USA: ")
region= str(region)
if region == "EUR" and wiek > 18:
    print("pochodzisz z regionu EUR i masz wiecej niż 18 lat wiec dostajesz super ceny dla EUR")
elif region == "USA" and wiek > 21:
    print("pochodzisz z regionu USA i masz wiecej niż 21 lat wiec dostajesz super ceny dla USA")
elif region !="EUR" and wiek>18:
    print("nie pochodzisz z regionu EUR i  ale masz więcej niż 18 wiec nie dostajesz super ceny dla EUR")
elif region!="USA" and wiek>21:
    print(" nie pochodzisz z regionu usa ale masz wiecej niz 21 , wiec nie dostajesz ceny dla usa")
elif region =="EUR" and wiek <18:
    print("pochodzisz z regionu EUR ale masz 18 lub mniej lat wiecj nie dostajesz super ceny dla USA ")
elif region =="USA" and wiek <21:
    print("pochodzisz z regionu USA ale masz 21 lub mniej lat wiecj nie dostajesz super ceny dla usa")
    
imie = input("Podaj Imię: ")
print ("Czesc", imie)

plec = input("Podaj swoją płeć (M/K)")
plec = str(plec)
if plec == "M":
	print ("jestes menem")
if plec == "K":
	print ("jestes kobieta")
else:
    print("Błędne dane, wprowadz ponownie")
