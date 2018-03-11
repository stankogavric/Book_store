from korisnici import *

def provjera_korisnik(korisnik1, lozinka):
    # funkcija koja vrši provjeru prilikom prijave na sistem, da li uneseno korisničko ime i lozinka odgovaraju nekom od registrovanih korisnika
    global lista_korisnika
    global korisnik_temp
    korisnik_temp = {}
    
    for korisnik in lista_korisnika:
        if korisnik["korisnicko_ime"] == korisnik1 and korisnik["sifra"] == lozinka:
            
            korisnik_temp["ime_temp"] = korisnik["ime"]
            
            korisnik_temp["prezime_temp"] = korisnik["prezime"]
            
            korisnik_temp["uloga_temp"] = korisnik["uloga"]

            return False

    return True
