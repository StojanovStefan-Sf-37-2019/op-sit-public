import autododaj
from datetime import date
from datetime import datetime
import random
import ocene

def meni_rezervacije():
    print("\n```````````````````````````````````````")
    print("[1] Kreiraj rezervaciju             ```")
    print("[2] Pregled rezervacija             ```")
    print("[3] Oceni rezervaciju               ```")
    print("[4] Pregled Automobila              ```")
    print("[5] Pretraga Automobila             ```")
    print("[6] Prikaz najbolje ocenjenih auta  ```")
    print("[x] Izlaz                           ```")
    print("```````````````````````````````````````")

    x = input("\nUnesi opciju: ").lower()
    if x == "1":
        cuvanje()
    if x== "2":
        pregled_rezervacije()
        return meni_rezervacije()
    if x=="3":
        oceni_pocetna()

    if x =="4":
        autododaj.ispisi_auto()
        return meni_rezervacije()
    if x =="5":
        autododaj.pretraga_automobila()
    if x=="6":
        ocene.svi_auti()
        ocene.rejting()
        meni_rezervacije()
    if x == "x":
        return 0

def sifra():
    kod = random.randint(100000,999999)
    return kod

def nova_rezervacija():
    ras = raspolozivo()
    print("\n`````````````````````````````````````````")
    print("`````Popunjavanj nove rezervacije````````````````````````````````")
    id_1 = input("Unesite ID Auta")
    f = open("txt_fajlovi/rezervacije.txt","r")
    lines = f.readlines()
    for line in lines:
        spliti = line.split("|")
        if id_1 in spliti:
            print("Zauzeto")
            nova_rezervacija()
            break
        else:
            pass
    id = str(provera_id())
    user = str(provera_username())
    user1 = input("Unesite kontakt username na koga se vodi rezervacija: ")
    kod = sifra()
    datumi1 = okej_datumi()
    splitovano1 = datumi1[0]
    splitovano2 = datumi1[1]
    print(">>Uspesno Kreirana Rezervacija!`````````````````````````````````")
    sve = str(kod)+"|"+id_1+"|"+user1 +"|" +splitovano1+"|"+splitovano2+"\n"
    jos_jednom = rez_opet()
    return sve
    return id_1

def raspolozivo():
    x = input("Zelite li videti raspolozive auto da/ne: ")
    if x == "da":
        autododaj.ispisi_auto()
        return
    else:
        pass

def rez_opet():
    x = input("\nDa li zelite izvrsiti jos jednu rezervaciju: Da/Ne: ").lower()
    if x == "da":
        nova_rezervacija()
    elif x== "ne":
        pass
    else:
        print("\nUnesite nesto od ponudjenog")

def cuvanje():
    date = vreme_sada()
    tu = nova_rezervacija()
    f_in = open("txt_fajlovi/rezervacije.txt","a")
    sve = date + "|"+tu
    print(sve)
    stamp =f_in.write(sve)
    dalje = meni_rezervacije()

def pregled_rezervacije():
    print("\n````````````````````````````````````````")
    print("Provera: ")
    id = ispis_provera()

def vreme():
    datum = str(date.today())
    return datum

def vreme_sada():
    datum = str(datetime.now())
    date = datum.split()[0]
    h,m = [datum.split()[1].split(":")[0],datum.split()[1].split(":")[1]]

    return date + " " + h + ":" + m

def oceni_pocetna():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nRezervacija se moze oceniti samo kad je zavrsena        ~")
    print("\nUnesite datum kada ste vratili automobil                ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    date1 = vreme()
    date2 = datum_vracanja()
    if date1>date2:
        print("\nProslo je")
        ocenjivanje()
    else:
        print("\nRezervacija i dalje traje..")
        return 0

def ocenjivanje():
    print("********************************************************")
    print("Ocenjivanje se vrsi od ocenom od 1-5                 ***")
    fajl = open("txt_fajlovi/ocene.txt","a")
    ocena = str(unos_ocene())
    model = input("Unesite ID Auta kog ste iznajmili: ")
    sve = model + "|" + ","+ocena + "\n"
    print("Hvala vam sto se ocenili rezervaciju i time podrzali nas salon!")
    dalje = meni_rezervacije()
    return ocena

def unos_ocene():
    x = input("\nUnesi ocenu: ")
    if x=="1" or x=="2" or x =="3" or x=="4" or x =="5":
        print("~~~~~~~~~~~")
        pass
    else:
        print("Ocene moraju biti od 1-5")
        unos_ocene()
    return x

def datum_vracanja():
    print("\n`````````Unesite datum Kada ste vratili automobil````````````")
    print("Datum mora biti u\nformatu -Godina/Mesec/Dan-              ``")
    godina = str(2020)
    mesec = input("Unesite mesec: \nPrimer: *Januar-01*:\n")
    dan = input("Unesite dan-\n*Primer:28*:\n")
    sve2 = godina + "-" + mesec +"-" + dan +"\n"
    f = open("txt_fajlovi/rezervacije.txt","r")
    lines = f.readlines()
    uspesnost = False
    for line in lines:
        spliti = line.split("|")
        if sve2 in spliti:
            print("\nPostoji takva rezervacija                    ``")
            ocenjivanje()
            uspesnost = True
            break
    if uspesnost == False:
        print("\nNe postoji takva rezervacija!")
        meni_rezervacije()

    return sve2

def ispis_provera():
    f_in = open("txt_fajlovi/rezervacije.txt","r")
    cars = f_in.readlines()
    print("Unesite username")
    print("\n")
    opcija = input("Opcija: ")
    for car in cars:
        split = car.split("|")
        uspesnost = False
        if opcija in split:
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format("Vreme izdavanja","Sifra","ID Auta","Korisnik","Vreme uzimanja","Vreme povratka"))
            print(80*'``')
            ident,brtab,naziv,model,mesta,mesta2= split[0], split[1], split[2],split[3],split[4],split[5],
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format(ident,brtab,naziv,model,mesta,mesta2))
            print("\n")
            uspesnost = True
            return
    if uspesnost == False:
        print("Nema")
        ispis_provera()

def ispis_provera2():
    f_in = open("txt_fajlovi/rezervacije.txt","r")
    cars = f_in.readlines()
    print("\n*****************************************************************************************")
    print("Dostupne su visestruke pretrage po datumu, po vremenu izdavanje, po korisniku    ********")
    print("Unesite info\n")
    opcija1 = input("Opcija 1: ")
    opcija2 = input("Opcija 2:")
    print("*****************************************************************************************")
    for car in cars:
        split = car.split("|")
        uspesnost = False
        if opcija1 in split and opcija2 in split:
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format("Vreme izdavanja","Sifra","ID Auta","Korisnik","Vreme uzimanja","Vreme povratka"))
            print(80*'``')
            ident,brtab,naziv,model,mesta,mesta2= split[0], split[1], split[2],split[3],split[4],split[5],
            print('{0:<30}{1:<25}{2:<25}{3:<25}{4:<25}{5:<25}'.format(ident,brtab,naziv,model,mesta,mesta2))
            print("\n")
            uspesnost = True
            return
            break
    if uspesnost == False:
        print("Nema")
        return

def zaposleni_rezervacije():
    print("\nDostupne je jednostruka i dvostruka pretraga***********************")
    print("[1] Jednostruka                             ***********************")
    print("[2] Dvostruka                               ***********************")
    print("[x] Nazad                                   ***********************")
    x = input("\nUnesite opciju: ").lower()
    if x == "1":
        ispis_provera()
        zaposleni_rezervacije()
    if x=="2":
        ispis_provera2()
        zaposleni_rezervacije()
    if x=="x":
        return
    else:
        print("\nUnesite neku od opcija")

def provera_username():
    user = input("\nUnesite vas Username radi provere:")
    f_in = open("txt_fajlovi/korisnici.txt","r")
    lines = f_in.readlines()
    for line in lines:
        sve = line.split("|")
        provera = False
        if user in sve:
            print("\nValidan")
            provera = True
            break
    if provera == False:
        print("\nNe postoji takav korisnik")
        provera_username()

        return user

def provera_id():

    f_in = open("txt_fajlovi/automobilii.txt","r")
    lines = f_in.readlines()
    id_auta = input("Potvrdite unos ID:")
    for line in lines:
        sve = line.split("|")
        provera = False
        if id_auta in sve:
            print("Postoji")
            provera = True
            break
    if provera == False:
        print("Nema")
        provera_id()
        return id_auta

def preuzimanje_datum():
    print("\n````Unesite datum preuzimanja```````")
    print("Datum mora biti u\nformatu -Godina/Mesec/Dan-")
    godina = str(2020)
    mesec = input("Unesite mesec -\nPrimer *Januar je 01*\n: ")
    if int(mesec)>12:
        print("Nema toliko meseci")
        preuzimanje_datum()
    else:
        pass
    dan = input("Unesite dan- \n*Primer:28\n: ")
    if int(dan)>31:
        print("Nema toliko dana")
        preuzimanje_datum()
        False
    else:
        pass
    sve1 = godina + "-" + mesec +"-" + dan
    return sve1

def povratak_datum():
    print("\n````Unesite datum Povratka```````")
    print("Datum mora biti u\nformatu -Godina/Mesec/Dan-")
    godina = str(2020)
    mesec = input("Unesite mesec: Januar-01:\n")
    if int(mesec)>12:
        print("Nema toliko meseci")
        povratak_datum()
    else:
        pass
    dan = input("Unesite dan-Primer:28:\n")
    if int(dan)>31:
        print("Nema toliko dana")
        povratak_datum()
    else:
        pass
    sve2 = godina + "-" + mesec +"-" + dan
    return sve2

def prikaz_svih_rezervacija():
	rezervacije = open("txt_fajlovi/rezervacije.txt", "r")
	print('{0:<35}{1:<23}{2:<25}{3:<35}{4:<23}{5:<25}'.format("Vreme izdavanja","Sifra rezervacije","ID Auta","Na koga se vodi","Vreme preuzimanje","Vreme vracanja"))
	print(160*'*')
	for i, auto in enumerate(rezervacije):
		podaci = auto.split('|')
		ident,brtab,naziv,vodenje,sifra,sifra2= podaci[0], podaci[1], podaci[2],podaci[3],podaci[4],podaci[5],
		print('{0:<35}{1:<23}{2:<25}{3:<35}{4:<23}{5:<25}'.format(ident,brtab,naziv,vodenje,sifra,sifra2))

def okej_datumi():
    datesada = vreme()
    date1 = preuzimanje_datum()
    date2 = povratak_datum()
    if date1<date2 and date1>datesada:
        print("Datumi su okej")
    else:
        print("\nDatumi se ne podudaraju!!")
        print("Probajte ponovo!")
        okej_datumi()
    return date1,date