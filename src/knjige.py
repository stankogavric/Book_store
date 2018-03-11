# -*- coding: utf-8 -*-

from provjeri_unos import *
import os

def parsiraj_knjigu(line):
    # funkcija koja od linije formata autori|naslov|godina|isbn|zanr|cijena|kolicina|opis|brisanje kreira i vraća rječnik s podacima o jednoj knjizi
    knjiga = {}

    podaci = line.split("|")
    # parsiranje linije po karakteru "|", što znači da nijedan od podataka ne smije da sadrži karakter "|"

    if len(podaci) != 9:
        print("Pogrešan format fajla u kome se čuvaju knjige!")
    else:
        knjiga["autori"] = podaci[0]
        knjiga["naslov"] = podaci[1]
        knjiga["godina"] = podaci[2]
        knjiga["isbn"] = podaci[3]
        knjiga["zanr"] = podaci[4]
        knjiga["cijena"] = podaci[5]
        knjiga["kolicina"] = podaci[6]
        knjiga["opis"] = podaci [7]
        knjiga["brisanje"] = podaci [8]

    return knjiga

def ucitavanje_knjiga(file_name):
    # funkcija koja učitava knjige i kreira i vraća listu knjiga
    # file_name je apsolutna ili relativna putanja do fajla

    lista_knjiga = []
    # lista svih knjiga
    
    if os.path.exists(file_name):
        file = open(file_name, "r")
        # otvaranje fajla u modu za čitanje

        for line in file:
            l = line.strip()
            # za uklanjanje svih nepotrebnih razmaka s početka i kraja
            knjiga = parsiraj_knjigu(l)
            # kreiranje jednog rječnika koji vraća podatke o jednoj knjizi

            lista_knjiga.append(knjiga)
            # dodavanje knjige u listu knjiga
            
        file.close()
        # zatvaranje otvorenog fajla
        
    else:
        path_parts = file_name.split("/")
        dirs = "/".join(path_parts[:-1])
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        f = open(file_name, "w")
        f.close()

        file = open(file_name, "r")
        # otvaranje fajla u modu za čitanje

        for line in file:
            l = line.strip()
            # za uklanjanje svih nepotrebnih razmaka s početka i kraja
            knjiga = parsiraj_knjigu(l)
            # kreiranje jednog rječnika koji vraća podatke o jednoj knjizi

            lista_knjiga.append(knjiga)
            # dodavanje knjige u listu knjiga
            
        file.close()
        # zatvaranje otvorenog fajla
    
    return lista_knjiga

lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")

def unos_knjiga():
    # funkcija koja služi za unos novih knjiga
    global lista_knjiga
    zanrovi = ["autobiografija", "drama", "fantazija", "roman"]
    knjiga = {}
    
    print("\n-----Podaci o knjizi-----")

    autori = input("Autori: ")
    autori = provjeri_unos(autori)
    knjiga["autori"] = autori

    naslov = input("Naslov: ")
    naslov = provjeri_unos(naslov)
    knjiga["naslov"] = naslov

    godina = None
    while godina is None:
        x = input ("Godina: ")
        if x.isdigit():
            godina = x
            knjiga["godina"] = godina
        else:
            print("Godina mora biti broj")

    isbn = None
    while isbn is None:
        unos_isbn = input("ISBN: ")
        if unos_isbn.isdigit() and provjera_isbn(unos_isbn):
            isbn = unos_isbn
            knjiga["isbn"] = isbn
        else:
            print("Unijeti isbn već postoji ili je pogrešan format unosa. Pokušajte ponovo.")

    zanr = None
    while zanr is None:
        print("Ponuđeni žanrovi:")
        for i in range(len(zanrovi)):
            print(str(i+1) + ".) " + zanrovi[i])

        zanr_indeks = input("Unesite redni broj žanra: ")
        if zanr_indeks.isdigit():
            if 0 < int(zanr_indeks) <= len(zanrovi):
                zanr = zanrovi[int(zanr_indeks) - 1]
                knjiga["zanr"] = zanr
        else:
            print("\nIndeks žanra mora biti broj")

    cijena = None
    while cijena is None:
        x = input("Cijena: ")
        try:
            cijena = float(x)
            knjiga["cijena"] = cijena
        except ValueError:
            print("Pogrešan format unosa. Pokušajte ponovo.")

    kolicina = None
    while kolicina is None:
        x = input("Količina: ")
        if x.isdigit():
            kolicina = int(x)
            knjiga["kolicina"] = kolicina
        else:
            print("Količina mora biti pozitivan cijeli broj")

    opis = input("Opis: ")
    opis = provjeri_unos(opis)
    knjiga["opis"] = opis
    
    knjiga["brisanje"] = False
  
    lista_knjiga.append(knjiga)
    # dodavanje knjige u listu knjiga

    zapis = "{}|{}|{}|{}|{}|{:.2f}|{}|{}|{}\n".format(knjiga["autori"], knjiga["naslov"], knjiga["godina"], knjiga["isbn"], knjiga["zanr"],
                                                     float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"], knjiga["brisanje"])

    print("\nUnesena knjiga:")
    print(knjiga)
    print("\nZapis unesene knjige u fajlu:")
    print(zapis)

    f = open("../data/fajl_knjige.txt", "a")
    f.write(zapis)
    f.close()

    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")

    print("Učitane knjige:")
    for knjiga in lista_knjiga:
        print(knjiga)

def provjera_isbn(isbn):
    # funkcija koja vrši provjeru da li uneseni ISBN već postoji
    global lista_knjiga

    for knjiga in lista_knjiga:
        if knjiga["isbn"] == isbn:
            return False

    return True

def lista_isbn():
    #funkcija koja kreira i vraća listu isbn-ova
    global lista_knjiga
    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")
    lista_isbn=[]
    for knjiga in lista_knjiga:
        if (knjiga["brisanje"] == "False" and int(knjiga["kolicina"]) > 0):
            lista_isbn.append(knjiga["isbn"])
    return lista_isbn

def lista_naslova():
    #funkcija koja kreira i vraća listu naslova
    global lista_knjiga
    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")
    lista_naslova=[]
    for knjiga in lista_knjiga:
        if (knjiga["brisanje"] == "False" and int(knjiga["kolicina"]) > 0):
            if (knjiga["naslov"] not in lista_naslova):
                lista_naslova.append(knjiga["naslov"])
    return lista_naslova

def lista_zanrova():
    #funkcija koja kreira i vraća listu žanrova
    global lista_knjiga
    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")
    lista_zanrova=[]
    for knjiga in lista_knjiga:
        if (knjiga["brisanje"] == "False" and int(knjiga["kolicina"]) > 0):
            if (knjiga["zanr"] not in lista_zanrova):
                lista_zanrova.append(knjiga["zanr"])
    return lista_zanrova

def lista_autora():
    #funkcija koja kreira i vraća listu autora
    global lista_knjiga
    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")
    lista_autora=[]
    for knjiga in lista_knjiga:
        if (knjiga["brisanje"] == "False" and int(knjiga["kolicina"]) > 0):
            if (knjiga["autori"] not in lista_autora):
                lista_autora.append(knjiga["autori"])
    return lista_autora

def pretraga_isbn():
    #funkcija koja vrši pretragu knjiga po ISBN-u
    global lista_knjiga
    lista=lista_isbn()
    x = True
    while x:
        ulaz = input ("Unesite ISBN za pretraživanje: ")
        ulaz = provjeri_unos(ulaz)
        if ulaz.isdigit():
            x = False
        else:
            print("Pogrešan format unosa. Pokušajte ponovo.")
    n = len (lista)
    i = 0
    ind = True
    print("\nISBN            NASLOV          AUTORI          GODINA IZDAVANJA ŽANR            CIJENA  KOLIČINA OPIS           ")
    while ind:
        if (i<n):
            if (lista[i].find(ulaz) != -1): 
                for knjiga in lista_knjiga:
                    if (lista_isbn()[i]==knjiga["isbn"]):
                        print("{:<15} {:<15} {:<15} {:<16} {:<15} {:<7.2f} {:<8} {:<15}".format(knjiga["isbn"], knjiga["naslov"], knjiga["autori"], knjiga["godina"],
                                                                                             knjiga["zanr"], float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"]))
            i = i + 1
        else:
            ind = False
            
def pretraga_naslov():
    #funkcija koja vrši pretragu knjiga po naslovu
    global lista_knjiga
    lista = lista_naslova()
    for i in range(len(lista)):
        lista[i]=lista[i].upper()
    ulaz = input ("Unesite naslov za pretraživanje: ")
    ulaz = provjeri_unos(ulaz).upper()
    n = len (lista)
    i = 0
    ind = True
    print("\nISBN            NASLOV          AUTORI          GODINA IZDAVANJA ŽANR            CIJENA  KOLIČINA OPIS           ")
    while ind:
        if (i<n):
            if (lista[i].find(ulaz) != -1): 
                for knjiga in lista_knjiga:
                    if (lista_naslova()[i]==knjiga["naslov"]):
                        print("{:<15} {:<15} {:<15} {:<16} {:<15} {:<7.2f} {:<8} {:<15}".format(knjiga["isbn"], knjiga["naslov"], knjiga["autori"], knjiga["godina"],
                                                                                             knjiga["zanr"], float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"]))
            i = i + 1
        else:
            ind = False

def pretraga_zanr():
    #funkcija koja vrši pretragu knjiga po žanru
    global lista_knjiga
    lista = lista_zanrova()
    for i in range(len(lista)):
        lista[i]=lista[i].upper()
    ulaz = input ("Unesite žanr za pretraživanje: ")
    ulaz = provjeri_unos(ulaz).upper()
    n = len (lista)
    i = 0
    ind = True
    print("\nISBN            NASLOV          AUTORI          GODINA IZDAVANJA ŽANR            CIJENA  KOLIČINA OPIS           ")
    while ind:
        if (i<n):
            if (lista[i].find(ulaz) != -1): 
                for knjiga in lista_knjiga:
                    if (lista_zanrova()[i]==knjiga["zanr"]):
                        print("{:<15} {:<15} {:<15} {:<16} {:<15} {:<7.2f} {:<8} {:<15}".format(knjiga["isbn"], knjiga["naslov"], knjiga["autori"], knjiga["godina"],
                                                                                             knjiga["zanr"], float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"]))
            i = i + 1
        else:
            ind = False

def pretraga_autor():
    #funkcija koja vrši pretragu knjiga po autoru
    global lista_knjiga
    lista=lista_autora()
    for i in range(len(lista)):
        lista[i]=lista[i].upper()
    ulaz = input ("Unesite autora za pretraživanje: ")
    ulaz = provjeri_unos(ulaz).upper()
    n = len (lista)
    i = 0
    ind = True
    print("\nISBN            NASLOV          AUTORI          GODINA IZDAVANJA ŽANR            CIJENA  KOLIČINA OPIS           ")
    while ind:
        if (i<n):
            if (lista[i].find(ulaz) != -1): 
                for knjiga in lista_knjiga:
                    if (lista_autora()[i]==knjiga["autori"]):
                        print("{:<15} {:<15} {:<15} {:<16} {:<15} {:<7.2f} {:<8} {:<15}".format(knjiga["isbn"], knjiga["naslov"], knjiga["autori"], knjiga["godina"],
                                                                                             knjiga["zanr"], float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"]))
            i = i + 1
        else:
            ind = False

def brisanje_knjige():
    #funkcija koja vrši brisanje knjige
    global lista_knjiga
    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")
    nova_lista_knjiga = []
    for knjiga in lista_knjiga:
        if (knjiga["brisanje"] == "False" and int(knjiga["kolicina"]) > 0):
            nova_lista_knjiga.append(knjiga)
    if (nova_lista_knjiga == []):
        print("\nNema knjiga za brisanje")
        return
    x = True
    while(x):
        i = 1
        print("\nSpisak knjiga:\n")
        print("RB. ISBN            NASLOV       ")
        for knjiga in nova_lista_knjiga:
            print("{:>2}. {:<15} {:<15}".format(i, knjiga["isbn"], knjiga["naslov"]))
            i = i + 1
        ulaz = input("\nUnesite redni broj knjige za brisanje: ")
        if ulaz.isdigit():
            if 0 < int(ulaz) <= len(nova_lista_knjiga):
                ulaz = int(ulaz)
                x = False
            else:
                print("\nPogrešan unos")
    for i in range(len(nova_lista_knjiga)):
        if (ulaz == i+1):
            for knjiga in lista_knjiga:
                if (nova_lista_knjiga[i]["isbn"] == knjiga["isbn"]):
                    knjiga["brisanje"] = True
    f = open("../data/fajl_knjige.txt", "w")
    for knjiga in lista_knjiga:
        zapis = "{}|{}|{}|{}|{}|{:.2f}|{}|{}|{}\n".format(knjiga["autori"], knjiga["naslov"], knjiga["godina"], knjiga["isbn"], knjiga["zanr"],
                                                         float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"], knjiga["brisanje"])
        f.write(zapis)
    f.close()
    print("\nKnjiga je uspiješno izbrisana")

def izmjena_knjige():
    #funkcija koja vrši izmjenu knjige
    global lista_knjiga
    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")
    nova_lista_knjiga = []
    for knjiga in lista_knjiga:
        if (knjiga["brisanje"] == "False" and int(knjiga["kolicina"]) > 0):
            nova_lista_knjiga.append(knjiga)
    if (nova_lista_knjiga == []):
        print("\nNema knjiga za izmjenu")
        return
    x = True
    while(x):
        i = 1
        print("\nSpisak knjiga:\n")
        print("RB. ISBN            NASLOV       ")
        for knjiga in nova_lista_knjiga:
            print("{:>2}. {:<15} {:<15}".format(i, knjiga["isbn"], knjiga["naslov"]))
            i = i + 1
        ulaz = input("\nUnesite redni broj knjige: ")
        if ulaz.isdigit():
            if 0 < int(ulaz) <= len(nova_lista_knjiga):
                ulaz = int(ulaz)
                x = False
            else:
                print("\nPogrešan unos")
    for i in range(len(nova_lista_knjiga)):
        if (ulaz == i+1):
            for knjiga in lista_knjiga:
                if (nova_lista_knjiga[i]["isbn"] == knjiga["isbn"]):
                    #izmjena podataka o knjizi
                    
                    zanrovi = ["autobiografija", "drama", "fantazija", "roman"]
                    
                    print("\n-----Podaci o knjizi-----")
                    
                    autori = input("Autori: ")
                    autori = provjeri_unos(autori)
                    knjiga["autori"] = autori
                    
                    naslov = input("Naslov: ")
                    naslov = provjeri_unos(naslov)
                    knjiga["naslov"] = naslov
                    
                    godina = None
                    while godina is None:
                        x = input ("Godina: ")
                        if x.isdigit():
                            godina = x
                            knjiga["godina"] = godina
                        else:
                            print("Godina mora biti broj")
                            
                    zanr = None
                    while zanr is None:
                        print("Ponuđeni žanrovi:")
                        for i in range(len(zanrovi)):
                            print(str(i+1) + ".) " + zanrovi[i])
                            
                        zanr_indeks = input("Unesite redni broj žanra: ")
                        if zanr_indeks.isdigit():
                            if 0 < int(zanr_indeks) <= len(zanrovi):
                                zanr = zanrovi[int(zanr_indeks) - 1]
                                knjiga["zanr"] = zanr
                        else:
                            print("\nIndeks žanra mora biti broj")
                    
                    cijena = None
                    while cijena is None:
                        x = input("Cijena: ")
                        try:
                            cijena = float(x)
                            knjiga["cijena"] = cijena
                        except ValueError:
                            print("Pogrešan format unosa. Pokušajte ponovo.")
                    
                    kolicina = None
                    while kolicina is None:
                        x = input("Količina: ")
                        if x.isdigit():
                            kolicina = int(x)
                            knjiga["kolicina"] = kolicina
                        else:
                            print("Količina mora biti pozitivan cijeli broj")
                    
                    opis = input("Opis: ")
                    opis = provjeri_unos(opis)
                    knjiga["opis"] = opis
                    
                    break
                    
    f = open("../data/fajl_knjige.txt", "w")
    for knjiga in lista_knjiga:
        zapis = "{}|{}|{}|{}|{}|{:.2f}|{}|{}|{}\n".format(knjiga["autori"], knjiga["naslov"], knjiga["godina"], knjiga["isbn"], knjiga["zanr"],
                                                         float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"], knjiga["brisanje"])
        f.write(zapis)
    f.close()
    print("\nKnjiga je uspiješno izmijenjena")
