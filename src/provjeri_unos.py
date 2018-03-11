def provjeri_unos(string):
    # funkcija koja vrši provjeru da li je uneseni podatak prazan
    while string=="" or string.isspace():
         string=input("Traženi podatak ne smije biti prazan. Unesite ponovo: ")
    return string
