# -*- coding: utf-8 -*-

import time
import provjeri_prijavu
from provjeri_unos import *
from knjige import *
import os

def parsiraj_racun(line):
    # funkcija koja od linije formata sifra|datum|vrijeme|ukupna_cijena|prodavac kreira i vraća rječnik s podacima o jednom računu
    racun = {}

    podaci = line.split("|")
    # parsiranje linije po karakteru "|", što znači da nijedan od podataka ne smije da sadrži karakter "|"
    
    if len(podaci) != 5:
        print("Pogrešan format fajla u kome se čuvaju računi!")
    else:
        racun["sifra"] = podaci[0]
        racun["datum"] = podaci[1]
        racun["vrijeme"] = podaci[2]
        racun["ukupna_cijena"] = podaci[3]
        racun["prodavac"] = podaci [4]

    return racun

def ucitavanje_racuna(file_name):
    # funkcija koja učitava račune i kreira i vraća listu računa
    # file_name je apsolutna ili relativna putanja do fajla

    lista_racuna = []
    # lista svih računa
    
    if os.path.exists(file_name):
        file = open(file_name, "r")
        # otvaranje fajla u modu za čitanje
        
        for line in file:
            l = line.strip()
            # za uklanjanje svih nepotrebnih razmaka s početka i kraja
            racun = parsiraj_racun(l)
            # kreiranje jednog rječnika koji vraća podatke o jednom računu
            
            lista_racuna.append(racun)
            # dodavanje računa u listu računa
            
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
            racun = parsiraj_racun(l)
            # kreiranje jednog rječnika koji vraća podatke o jednom računu
            
            lista_racuna.append(racun)
            # dodavanje računa u listu računa
            
        file.close()
        # zatvaranje otvorenog fajla
        
    return lista_racuna

lista_racuna = ucitavanje_racuna("../data/fajl_racuni.txt")

def unos_racuna():
    # funkcija koja služi za unos novih računa
    global lista_racuna
    racun = {}
    
    print("\n-----Podaci o računu-----")
    
    racun["sifra"] = len(lista_racuna) + 1

    racun["datum"] = time.strftime("%d.%m.%Y.")
    racun["vrijeme"] = time.strftime("%H:%M:%S")

    racun["prodavac"] = provjeri_prijavu.korisnik_temp["ime_temp"] + " " + provjeri_prijavu.korisnik_temp["prezime_temp"]

    ukupna_cijena = None
    while ukupna_cijena is None:
        x = input("Ukupna cijena: ")
        try:
            ukupna_cijena = float(x)
            racun["ukupna_cijena"] = ukupna_cijena
        except ValueError:
            print("Pogrešan format unosa. Pokušajte ponovo.")

    lista_racuna.append(racun)
    # dodavanje računa u listu računa

    zapis = "{}|{}|{}|{:.2f}|{}\n".format(racun["sifra"], racun["datum"], racun["vrijeme"], float(racun["ukupna_cijena"]), racun["prodavac"])

    print("\nUneseni račun:")
    print(racun)
    print("\nZapis unesenog računa u fajlu:")
    print(zapis)

    f = open("../data/fajl_racuni.txt", "a")
    f.write(zapis)
    f.close()

    lista_racuna = ucitavanje_racuna("../data/fajl_racuni.txt")

    print("Učitani računi:")
    for racun in lista_racuna:
        print(racun)

def provjera_sifra(sifra):
    # funkcija koja vrši provjeru da li unesena šifra već postoji
    global lista_racuna

    for racun in lista_racuna:
        if racun["sifra"] == sifra:
            return False

    return True

ukupno = 0
racun_temp = []

def dodaj_na_racun():
    #funkcija koja vrši dodavanje knjige na račun
    global lista_knjiga
    global ukupno
    global racun_temp
    nova_lista_knjiga = []
    for knjiga in lista_knjiga:
        if (knjiga["brisanje"] == "False" and int(knjiga["kolicina"]) > 0):
            nova_lista_knjiga.append(knjiga)
    if (nova_lista_knjiga == []):
        print("\nNema knjiga za dodavanje na račun")
        return
    x = True
    while(x):
        i = 1
        print("\nSpisak knjiga:\n")
        print("RB. ISBN            NASLOV       ")
        for knjiga in nova_lista_knjiga:
            if int(knjiga["kolicina"]) > 0:
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
                        kolicina = None
                        while kolicina is None:
                            x = input("Količina: ")
                            if x.isdigit():
                                x = int(x)
                                if x > 0:
                                    if x <= int(knjiga["kolicina"]):
                                        kolicina = x
                                        if knjiga not in racun_temp:  
                                            racun_temp.append(knjiga)
                                        ukupno = ukupno + float(knjiga["cijena"]) * kolicina
                                        knjiga["kolicina"] = int(knjiga["kolicina"]) - kolicina
                                    else:
                                        print("Greška! Maksimalan broj knjiga koje se mogu kupiti je:", knjiga["kolicina"])
                                else:
                                    print("Količina mora biti pozitivan cijeli broj")
                            else:
                                print("Količina mora biti pozitivan cijeli broj")
                                
    print("\nKnjiga je uspiješno dodana na račun")

def izdaj_racun():
    # funkcija koja služi za izdavanje računa
    global lista_knjiga
    global lista_racuna
    global ukupno
    global racun_temp
    racun = {}
    originali = ucitavanje_knjiga("../data/fajl_knjige.txt")

    racun["sifra"] = len(lista_racuna) + 1

    racun["datum"] = time.strftime("%d.%m.%Y.")
    racun["vrijeme"] = time.strftime("%H:%M:%S")

    racun["prodavac"] = provjeri_prijavu.korisnik_temp["ime_temp"] + " " + provjeri_prijavu.korisnik_temp["prezime_temp"]

    racun["ukupna_cijena"] = ukupno

    lista_racuna.append(racun)
    # dodavanje računa u listu računa

    zapis = "{}|{}|{}|{:.2f}|{}\n".format(racun["sifra"], racun["datum"], racun["vrijeme"], float(racun["ukupna_cijena"]), racun["prodavac"])

    f = open("../data/fajl_racuni.txt", "a")
    f.write(zapis)
    f.close()

    print("=====================================================")
    print("KNJIŽARA GAVRIĆ")
    print("21000 NOVI SAD, JEVREJSKA 4")
    print("TEL: 021/123-1234")
    print("-----------------------------------------------------")
    print("{:^53}".format("HVALA NA POSJETI!"))
    print("{:^53}".format("Broj računa:"))
    print("{:^53}".format(racun["sifra"]))
    print("-----------------------------------------------------")
    for element in racun_temp:
        print("{} {}".format(element["isbn"], element["naslov"]))
        for knjiga in originali:
            if knjiga["isbn"] == element["isbn"]:
                print("{:>8}x{:<7.2f}{:>37.2f}".format(int(knjiga["kolicina"])-element["kolicina"], float(element["cijena"]), (int(knjiga["kolicina"])-element["kolicina"])*float(element["cijena"])))
    print("-----------------------------------------------------")
    print("ZA UPLATU: {:.2f}".format(ukupno))
    print(racun["datum"])
    print(racun["vrijeme"])
    print("-----------------------------------------------------")
    print("PRODAVAC:")
    print(racun["prodavac"])
    print("=====================================================")

    f = open("../data/fajl_knjige.txt", "w")
    for knjiga in lista_knjiga:
        zapis = "{}|{}|{}|{}|{}|{:.2f}|{}|{}|{}\n".format(knjiga["autori"], knjiga["naslov"], knjiga["godina"], knjiga["isbn"], knjiga["zanr"],
                                                         float(knjiga["cijena"]), knjiga["kolicina"], knjiga["opis"], knjiga["brisanje"])
        f.write(zapis)
    f.close()

    ukupno = 0
    racun_temp = []

def ponisti_racun():
    #funkcija koja služi za poništavanje do tada formiranog računa
    global lista_knjiga
    global ukupno
    global racun_temp
    ukupno = 0
    racun_temp = []
    lista_knjiga = ucitavanje_knjiga("../data/fajl_knjige.txt")

def izmjena_racuna():
    #funkcija koja vrši izmjenu računa
    global lista_racuna
    nova_lista_racuna = []
    for racun in lista_racuna:
        nova_lista_racuna.append(racun)
    if (nova_lista_racuna == []):
        print("\nNema računa za izmjenu")
        return
    x = True
    while(x):
        i = 1
        print("\nSpisak računa:\n")
        print("RB. ŠIFRA           DATUM           VRIJEME         PRODAVAC        UKUPNA CIJENA  ")
        for racun in nova_lista_racuna:
            print("{:>2}. {:<15} {:<15} {:<15} {:<15} {:<15.2f}".format(i, racun["sifra"], racun["datum"], racun["vrijeme"], racun["prodavac"], float(racun["ukupna_cijena"])))
            i = i + 1
        ulaz = input("\nUnesite redni broj računa: ")
        if ulaz.isdigit():
            if 0 < int(ulaz) <= len(nova_lista_racuna):
                ulaz = int(ulaz)
                x = False
            else:
                print("\nPogrešan unos")
    for i in range(len(nova_lista_racuna)):
        if (ulaz == i+1):
            for racun in lista_racuna:
                if (nova_lista_racuna[i]["sifra"] == racun["sifra"]):
                    #izmjena podataka o računu
                    
                    print("\n-----Podaci o računu-----")

                    racun["prodavac"] = input("Unesite prodavca: ")

                    ukupna_cijena = None
                    while ukupna_cijena is None:
                        x = input("Ukupna cijena: ")
                        try:
                            ukupna_cijena = float(x)
                            racun["ukupna_cijena"] = ukupna_cijena
                        except ValueError:
                            print("Pogrešan format unosa. Pokušajte ponovo.")
                                    
                    break
                    
    f = open("../data/fajl_racuni.txt", "w")
    for racun in lista_racuna:
        zapis = "{}|{}|{}|{:.2f}|{}\n".format(racun["sifra"], racun["datum"], racun["vrijeme"], float(racun["ukupna_cijena"]), racun["prodavac"])
        f.write(zapis)
    f.close()
    print("\nRačun je uspiješno izmijenjen")
