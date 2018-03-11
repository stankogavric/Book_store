# -*- coding: utf-8 -*-

from meni import *
import provjeri_prijavu

print()
print("=======================")
print("|  Prodavnica knjiga  |")
print("=======================")
print()
print("Prijava na sistem")
print()

korisnik1 = input("Korisničko ime:")
lozinka = input("Šifra:")

while provjeri_prijavu.provjera_korisnik(korisnik1, lozinka):
    korisnik1 = input("Korisničko ime:")
    lozinka = input("Šifra:")

prijava="\nUspiješno ste se prijavili kao {}, {} {}".format(provjeri_prijavu.korisnik_temp["uloga_temp"], provjeri_prijavu.korisnik_temp["ime_temp"], provjeri_prijavu.korisnik_temp["prezime_temp"])
print(prijava)

if(provjeri_prijavu.korisnik_temp["uloga_temp"] == "administrator"):
    glavni_meni()
elif(provjeri_prijavu.korisnik_temp["uloga_temp"] == "prodavac"):
    prodavac_meni()
elif(provjeri_prijavu.korisnik_temp["uloga_temp"] == "menadžer"):
    menadžer_meni()
