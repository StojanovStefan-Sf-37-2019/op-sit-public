import register
import autododaj
import azuriranje
import rezervacije
import ocene

def login_meni():
    while(True):
        print("\n************************")         
        print("[1] Uloguj se ")
        print("[2] Registruj se ")
        print("[3] Rezim gosta ")
        print("[4] Izlaz ")
        print("************************\n")

        x = input("Unesite datu opciju: ")

        if x == "1":
            print("\nUlogujte se:\n")
            loginovanje()

            pass
        elif x == "2":
            register.registrovanje()
            return meni_registrovani()
            pass
        elif x=="3":
            print("\nPrelazak u rezim gosta.\n")
            menigost()
            break
        elif x == "4":
            print("Izlaz")
            exit()
        else:
            print("Molim Vas unesite opciju 1-4.\n")
            pass

def menigost():
    print("\n******************************************")
    print("[1]Registruj se                           ")
    print("[2]Pregled automobila                     ")
    print("[3]Pretraga automobila                    ")
    print("[4]Prikaz najbolje ocenjenih automobila   ")
    print("[5]Izlaz                                  ")
    print("******************************************\n")
    x = input("\nUnesite opciju: ")
    if x == "1":
        register.registrovanje()
        meni_registrovani()
    if x == "2":
        autododaj.ispisi_auto()
        return menigost()
    if x == "3":
        pretraga_zaposleni_meni()
        x = input("\nZelite li nazad? da/ne: ").lower()
        if x=="da":
            menigost()
        else:
            autododaj.pretraga_automobila()
    if x == "4":
        ocene.rejting()
        return menigost()
    if x=="5":
        login_meni()
    else:
        print("\nUnesite nesto od ponudjenog")
        menigost()

def meni_registrovani():
    print("\n**********************************************")
    print("[1] Rezervacije                               ")
    print("[2] Pregled Automobila                        ")
    print("[3] Pretraga Automobila                       ")
    print("[4] Najbolje ocenjeni automobili              ")
    print("[5] Odjava sa sistema                         ")
    print("**********************************************\n")
    x = input("Unesite opciju.")
    if x == "1":
        rezervacije.meni_rezervacije()
        x = input("\nZelite li nazad? da/ne: ")
        if x == "da":
            meni_registrovani()
        else:
            rezervacije.meni_rezervacije()
    if x == "2":
        autododaj.ispisi_auto()
        meni_registrovani()
    if x == "3":
        pretraga_zaposleni_meni()
        x = input("\nZelite li nazad? da/ne")
        if x=="da":
            meni_registrovani()
        else:
            autododaj.pretraga_automobila()
    if x == "4":
        autododaj.ispisi_auto()
        ocene.rejting()
        meni_registrovani()

    if x =="5":
        login_meni()
    else:
        print("\nUnesite nesto od ponudjenog. ")
        return meni_registrovani()

def meni_admin():
    print("\n************************************************")
    print("[S] Informacije o salonu                        ")
    print("\n[1] Dodavanje novih automobila                ")
    print("\n[2] Dodavanje novih zaposlenih                ")
    print("\n[3] Pregled Automobila                        ")
    print("\n[4] Pretraga Automobila                       ")
    print("\n[5] Azuriranje salona                         ")
    print("\n[6] Brisanje Automobila                       ")
    print("\n[7] Brisanje zaposlenih                       ")
    print("\n[8] Pretraga zaposlenih                       ")
    print("\n[X] Odjava                                    ")
    print("************************************************\n")
    x = input("\nUnesite neku od opcija: ")
    if x == "s":
        azuriranje.info_salon()
        x = input("Dalje? da ne")
        if x=="da":
            meni_admin()
        else:
            return
    if x == "1":
        autododaj.main()
        g = input("\nZelite li videti raspolozive automobile? ")
        if g == "da":
            autododaj.ispisi_auto()
            meni_admin()
    if x == "2":
        register.dodavanje_zaposlenih()
        return meni_admin()
    if x=="3":
        autododaj.ispisi_auto()
        meni_admin()
    if x=="4":
        autododaj.pretraga_automobila()
        x = input("\nZelite li nazad? da/ne:")
        if x=="da":
            meni_admin()
        else:
            autododaj.pretraga_automobila()
    if x=="5":
        register.korisnici_ispis()
        register.pretraga_zaposlenih()
    if x == "6":
        autododaj.obrisi_auto()
        print("\nUspesno Obrisano")
        g = input("\nZelite li nazad: ")
        if g== "da":
            meni_admin()
    if x == "7":
        register.obrisi_zaposlenog()
        return meni_admin()
    if x=="8":
        register.pretraga_zaposlenih()
        return meni_admin()
    if x == "x":
        login_meni()
    else:
        print("\nMolimo vas unesite neku od opcija:")
        return meni_admin()

def meni_zaposleni():
    print("\n************************************************")
    print("[1] Pretraga automobila")
    print("[2] Pretraga rezervacija")
    print("[3] Izvestavanje")
    print("[4] Izlaz")
    print("*************************************************\n")
    x = input("\nUnesi neku od opcija: ")
    if x=="1":
        pretraga_zaposleni_meni()
        x = input("\nZelite li nazad? da/ne ")
        if x=="da":
            meni_zaposleni()
        else:
            autododaj.pretraga_automobila()
    if x == "2":
        rezervacije.prikaz_svih_rezervacija()
        rezervacije.zaposleni_rezervacije()
        x = input("\nZelite li nazad? da/ne")
        if x == "da":
            meni_zaposleni()
        else:
            rezervacije.zaposleni_rezervacije()

    if x=="3":
        print("\nNot Implemented...")
        meni_zaposleni()
    if x=="4":
        login_meni()
    else:
        print("\nMolimo vas unesi nesto od ponudjenog ")
        meni_zaposleni()

def loginovanje():
    f_in = open("txt_fajlovi/korisnici.txt","r")
    clanovi = f_in.readlines()
    ime = input("\nUnesite vase korisnicko ime: ")
    sifra = input("\nUnesite vasu sifru: ")
    uspesno_log = ""
    for clan in clanovi:
        clan = clan.strip().split("|")

        clan_ime = clan[0]
        clan_sifra = clan[1]                
        clan_uloga = clan[6]
        uspesno_log = False
        if ime == clan_ime and sifra==clan_sifra:   

            print("\n`````````````````````````````````````````")
            print("Uspesno Ulogovani")
            uspesno_log =True
            if clan_uloga == "1":           
                print(meni_registrovani())
            elif clan_uloga == "2":
                print(meni_zaposleni())
            else:
                print(meni_admin())
            return 0
                                
    if uspesno_log == False:
            print("\n")
            print("Pogresno korisnicko ime ili lozinka")
            print("Probajte ponovo\n")
            loginovanje()

def pretraga_zaposleni_meni():
    print("\nPretraga automobila: ")
    print("[1] Pretraga po jednoj opciji")
    print("[2] Visestruka pretraga")
    print("[0] Povratak nazad\n")
    x = input("\nUnesi opciju:")

    if x=="1":
        autododaj.pretraga_kriterujum_jedan()
        pretraga_zaposleni_meni()
    elif x == "2":
        autododaj.meni_visestruka()
        pretraga_zaposleni_meni()
    elif x== "0":
        meni_registrovani()

    else:
        print("\nUkucajte nesto od ponudjenog")
        pretraga_zaposleni_meni()             

def main():
    login_meni()
main()        

__name__ = "__main__"
