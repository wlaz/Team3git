wiek = input("Podaj wiek: ")

# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
if wiek >= 18:
    print("Witamy!")
region = input("Podaj region EUR lub USA: ")
region= str(region)
if region == "EUR" and wiek > 21:
    print("pochodzisz z regionu EUR i masz wiecej niż 21 lat wiec dostajesz super ceny dla EUR")
elif region == "USA" and wiek > 21:
    print("pochodzisz z regionu USA i masz wiecej niż 21 lat wiec dostajesz super ceny dla EUR")
elif region !="EUR" and wiek>21:
    print("nie pochodzisz z regionu EUR i  ale masz więcej niż 21 wiec nie dostajesz super ceny dla EUR")
elif region =="EUR" and wiek <=21:
    print("pochodzisz z regionu EUR ale masz 21 lub mniej lat wiecj nie dostajesz super ceny dla USA ")
elif region =="USA" and wiek <=21:
    print("pochodzisz z regionu USA ale masz 21 lub mniej lat wiecj nie dostajesz super ceny dla usa")


