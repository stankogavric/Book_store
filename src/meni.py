# -*- coding: utf-8 -*-

from racuni import *
from korisnici import *
from knjige import *

def prodavac_meni():
    # funkcija koja ispisuje glavni meni za ulogu prodavca
    print("\nIzaberite jednu od sledećih opcija:")
    print("  1 - Pretraga knjiga")
    print("  2 - Prodaja knjiga")
    print("  3 - Izlazak iz aplikacije")
    opcija = input("Unesite redni broj opcije: ")
    if opcija == "1":
        x = "prodavac meni"
        pretrazivanje_meni(x)
    elif opcija == "2":
        ponisti_racun()
        y = "prodavac meni"
        prodaja_meni(y)
    elif opcija == "3":
        exit()
    else:
        print("\nPogrešan unos")
        prodavac_meni()
        
def menadžer_meni():
    # funkcija koja ispisuje glavni meni za ulogu menadžera
    print("\nIzaberite jednu od sledećih opcija:")
    print("  1 - Pretraga knjiga")
    print("  2 - Unos nove knjige")
    print("  3 - Brisanje knjige")
    print("  4 - Izmjena knjige")
    print("  5 - Izlazak iz aplikacije")
    opcija = input("Unesite redni broj opcije: ")
    if opcija == "1":
        x = "menadžer meni"
        pretrazivanje_meni(x)
    elif opcija == "2":
        unos_knjiga()
        menadžer_meni()
    elif opcija == "3":
        brisanje_knjige()
        menadžer_meni()
    elif opcija == "4":
        izmjena_knjige()
        menadžer_meni()
    elif opcija == "5":
        exit()
    else:
        print("\nPogrešan unos")
        menadžer_meni()

def glavni_meni():
    # funkcija koja ispisuje glavni meni za ulogu administratora
    print("\nIzaberite jednu od sledećih opcija:")
    print("  1 - Unos podataka")
    print("  2 - Izmjena unijetih podataka")
    print("  3 - Pretraga knjiga")
    print("  4 - Prodaja knjiga")
    print("  5 - Brisanje knjige")
    print("  6 - Izlazak iz aplikacije")
    opcija = input("Unesite redni broj opcije: ")
    if opcija == "1":
        meni1()
    elif opcija == "2":
        meni2()
    elif opcija == "3":
        x = "glavni meni"
        pretrazivanje_meni(x)
    elif opcija == "4":
        ponisti_racun()
        y = "glavni meni"
        prodaja_meni(y)
    elif opcija == "5":
        brisanje_knjige()
        glavni_meni()
    elif opcija == "6":
        exit()
    else:
        print("\nPogrešan unos")
        glavni_meni()

def meni1():
    # funkcija koja ispisuje podmeni izborom opcije 1 u glavnom meniju administratora
    print("\nIZABERITE OPCIJU ZA UNOS")
    print("------------------------")
    print("  1 - Korisnici")
    print("  2 - Knjige")
    print("  3 - Računi")
    print("  4 - Povratak na glavni meni")
    opcija = input("Unesite redni broj opcije: ")
    if opcija == "1":
        unos_korisnika()
        meni1()
    elif opcija == "2":
        unos_knjiga()
        meni1()
    elif opcija == "3":
        unos_racuna()
        meni1()
    elif opcija == "4":
        glavni_meni()
    else:
        print("\nPogrešan unos")
        meni1()

def meni2():
    # funkcija koja ispisuje podmeni izborom opcije 2 u glavnom meniju administratora
    print("\nIZABERITE OPCIJU ZA IZMJENU")
    print("------------------------")
    print("  1 - Korisnici")
    print("  2 - Knjige")
    print("  3 - Računi")
    print("  4 - Povratak na glavni meni")
    opcija = input("Unesite redni broj opcije: ")
    if opcija == "1":
        izmjena_korisnika()
        meni2()
    elif opcija == "2":
        izmjena_knjige()
        meni2()
    elif opcija == "3":
        izmjena_racuna()
        meni2()
    elif opcija == "4":
        glavni_meni()
    else:
        print("\nPogrešan unos")
        meni2()
        
def pretrazivanje_meni(x):
    # funkcija koja ispisuje meni za pretragu knjiga
    # x je parametar funkcije koji određuje na koji meni se treba vratiti prilikom izvršavanja opcije 5
    print("\nKnjige se mogu pretraživati prema:")
    print("  1 - ISBN-u")
    print("  2 - Naslovu")
    print("  3 - Žanru")
    print("  4 - Autoru")
    print("-------------------------------")
    print("  5 - Povratak na glavni meni")
    print("-------------------------------")
    opcija = input("Unesite redni broj opcije: ")
    if opcija == "1":
        pretraga_isbn()
        pretrazivanje_meni(x)
    elif opcija == "2":
        pretraga_naslov()
        pretrazivanje_meni(x)
    elif opcija == "3":
        pretraga_zanr()
        pretrazivanje_meni(x)
    elif opcija == "4":
        pretraga_autor()
        pretrazivanje_meni(x)
    elif opcija == "5":
        if x == "glavni meni":
            glavni_meni()
        elif x == "prodavac meni":
            prodavac_meni()
        elif x == "menadžer meni":
            menadžer_meni()
    else:
        print("\nPogrešan unos")
        pretrazivanje_meni(x)
        
def prodaja_meni(y):
    # funkcija koja ispisuje meni za prodaju knjiga
    # y je parametar funkcije koji određuje na koji meni se treba vratiti prilikom izvršavanja opcije 5
    print("\nIzaberite jednu od sledećih opcija:")
    print("  1 - Dodaj na račun")
    print("  2 - Izdaj račun")
    print("  3 - Povratak na glavni meni")
    opcija = input("Unesite redni broj opcije: ")
    if opcija == "1":
        dodaj_na_racun()
        prodaja_meni(y)
    elif opcija == "2":
        izdaj_racun()
        prodaja_meni(y)
    elif opcija == "3":
        ponisti_racun()
        if y == "glavni meni":
            glavni_meni()
        elif y == "prodavac meni":
            prodavac_meni()
    else:
        print("\nPogrešan unos")
        prodaja_meni(y)
