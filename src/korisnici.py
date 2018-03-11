# -*- coding: utf-8 -*-

from provjeri_unos import *
import os

def parsiraj_korisnika(line):
    # funkcija koja od linije formata korisnicko_ime|šifra|ime|prezime|uloga kreira i vraća rječnik s podacima o jednom korisniku
    korisnik = {}

    podaci = line.split("|")
    # parsiranje linije po karakteru "|" što znači da nijedan od podataka ne smije da sadrži karakter "|"

    if len(podaci) != 5:
        print("Pogrešan format fajla u kome se čuvaju korisnici!")
    else:
        korisnik["korisnicko_ime"] = podaci[0]
        korisnik["sifra"] = podaci[1]
        korisnik["ime"] = podaci[2]
        korisnik["prezime"] = podaci[3]
        korisnik["uloga"] = podaci[4]

    return korisnik

def ucitavanje_korisnika(file_name):
    # funkcija koja učitava korisnike i kreira i vraća listu korisnika
    # file_name je apsolutna ili relativna putanja do fajla

    lista_korisnika = []
    # lista svih korisnika
    
    if os.path.exists(file_name):
        file = open(file_name, "r")
        # otvaranje fajla u modu za čitanje
        
        for line in file:
            l = line.strip()
            # za uklanjanje svih nepotrebnih razmaka s početka i kraja
            korisnik = parsiraj_korisnika(l)
            # kreiranje jednog rječnika koji vraća podatke o jednom korisniku

            lista_korisnika.append(korisnik)
            # dodavanje korisnika u listu korisnika

        file.close()
        # zatvaranje otvorenog fajla

    else:
        path_parts = file_name.split("/")
        dirs = "/".join(path_parts[:-1])
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        f = open(file_name, "w")
        f.write("admin|admin|Stanko|Gavrić|administrator\n")
        f.close()

        file = open(file_name, "r")
        # otvaranje fajla u modu za čitanje
        
        for line in file:
            l = line.strip()
            # za uklanjanje svih nepotrebnih razmaka s početka i kraja
            korisnik = parsiraj_korisnika(l)
            # kreiranje jednog rječnika koji vraća podatke o jednom korisniku

            lista_korisnika.append(korisnik)
            # dodavanje korisnika u listu korisnika

        file.close()
        # zatvaranje otvorenog fajla
        
    return lista_korisnika

lista_korisnika = ucitavanje_korisnika("../data/fajl_korisnici.txt")

def unos_korisnika():
    # funkcija koja služi za unos novih korisnika
    global lista_korisnika
    uloge = ["prodavac", "menadžer", "administrator"]
    korisnik = {}
    
    print("\n-----Podaci o korisniku-----")

    korisnicko_ime = None
    while korisnicko_ime is None:
        unos_korisnicko_ime = input("Korisničko_ime: ")
        unos_korisnicko_ime = provjeri_unos(unos_korisnicko_ime)

        if provjera_korisnicko_ime(unos_korisnicko_ime):
            korisnicko_ime = unos_korisnicko_ime
            korisnik["korisnicko_ime"] = korisnicko_ime
        else:
            print("Unijeto korisničko ime već postoji. Pokušajte ponovo.")
    
    sifra = input("Šifra: ")
    sifra = provjeri_unos(sifra)
    korisnik["sifra"] = sifra

    ime = input("Ime: ")
    ime = provjeri_unos(ime)
    korisnik["ime"] = ime

    prezime = input("Prezime: ")
    prezime = provjeri_unos(prezime)
    korisnik["prezime"] = prezime

    uloga = None
    while uloga is None:
        print("Ponuđene uloge:")
        for i in range(len(uloge)):
            print(str(i+1) + ".) " + uloge[i])

        uloga_indeks = input("Unesite redni broj uloge: ")
        if uloga_indeks.isdigit():
            if 0 < int(uloga_indeks) <= len(uloge):
                uloga = uloge[int(uloga_indeks) - 1]
                korisnik["uloga"] = uloga
        else:
            print("\nIndeks uloge mora biti broj")

    lista_korisnika.append(korisnik)
    # dodavanje korisnika u listu korisnika

    zapis = "{}|{}|{}|{}|{}\n".format(korisnik["korisnicko_ime"], korisnik["sifra"], korisnik["ime"], korisnik["prezime"], korisnik["uloga"])

    print("\nUneseni korisnik:")
    print(korisnik)
    print("\nZapis unesenog korisnika u fajlu:")
    print(zapis)

    f = open("../data/fajl_korisnici.txt", "a")
    f.write(zapis)
    f.close()

    lista_korisnika = ucitavanje_korisnika("../data/fajl_korisnici.txt")

    print("Učitani korisnici:")
    for korisnik in lista_korisnika:
        print(korisnik)

def provjera_korisnicko_ime(korisnicko_ime):
    # funkcija koja vrši provjeru da li uneseno korisničko ime već postoji
    global lista_korisnika

    for korisnik in lista_korisnika:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            return False

    return True

def izmjena_korisnika():
    #funkcija koja vrši izmjenu korisnika
    global lista_korisnika
    nova_lista_korisnika = []
    for korisnik in lista_korisnika:
        if korisnik["uloga"] != "administrator":
            nova_lista_korisnika.append(korisnik)
    if (nova_lista_korisnika == []):
        print("\nNema korisnika za izmjenu")
        return
    x = True
    while(x):
        i = 1
        print("\nSpisak korisnika:\n")
        print("RB. IME             PREZIME         KORISNIČKO IME ")
        for korisnik in nova_lista_korisnika:
            print("{:>2}. {:<15} {:<15} {:<15}".format(i, korisnik["ime"], korisnik["prezime"], korisnik["korisnicko_ime"]))
            i = i + 1
        ulaz = input("\nUnesite redni broj korisnika: ")
        if ulaz.isdigit():
            if 0 < int(ulaz) <= len(nova_lista_korisnika):
                ulaz = int(ulaz)
                x = False
            else:
                print("\nPogrešan unos")
    for i in range(len(nova_lista_korisnika)):
        if (ulaz == i+1):
            for korisnik in lista_korisnika:
                if (nova_lista_korisnika[i]["korisnicko_ime"] == korisnik["korisnicko_ime"]):
                    #izmjena podataka o korisniku
                    
                    uloge = ["prodavac", "menadžer", "administrator"]
                    
                    print("\n-----Podaci o korisniku-----")
                    
                    sifra = input("Šifra: ")
                    sifra = provjeri_unos(sifra)
                    korisnik["sifra"] = sifra

                    ime = input("Ime: ")
                    ime = provjeri_unos(ime)
                    korisnik["ime"] = ime

                    prezime = input("Prezime: ")
                    prezime = provjeri_unos(prezime)
                    korisnik["prezime"] = prezime

                    uloga = None
                    while uloga is None:
                        print("Ponuđene uloge:")
                        for i in range(len(uloge)):
                            print(str(i+1) + ".) " + uloge[i])

                        uloga_indeks = input("Unesite redni broj uloge: ")
                        if uloga_indeks.isdigit():
                            if 0 < int(uloga_indeks) <= len(uloge):
                                uloga = uloge[int(uloga_indeks) - 1]
                                korisnik["uloga"] = uloga
                        else:
                            print("\nIndeks uloge mora biti broj")
                                    
                    break
                    
    f = open("../data/fajl_korisnici.txt", "w")
    for korisnik in lista_korisnika:
        zapis = "{}|{}|{}|{}|{}\n".format(korisnik["korisnicko_ime"], korisnik["sifra"], korisnik["ime"], korisnik["prezime"], korisnik["uloga"])
        f.write(zapis)
    f.close()
    print("\nKorisnik je uspiješno izmijenjen")
