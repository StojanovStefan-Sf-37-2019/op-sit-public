import statistics
import autododaj

def svi_auti():
    print("\n Prikaz svih automobila: ")    
    autododaj.ispisi_auto()

def rejting():
    f_in = open("txt_fajlovi/ocene.txt","r")
    lines = f_in.readlines()
    ocene_lista = []
    ocenjena_lista = []

    for line in lines:
        grades = []
        line = line.split("|")

        id_auta = line[0]
        auto_ocene = line[1].strip("\n").split(",")
        for ocena_auta in auto_ocene:
            ocena = float(ocena_auta)
            grades.append(ocena)
        ocena = sum(grades)/len(grades)
        print("\n|   ID   |**************| Prosek Ocena |****************")
        print("|",id_auta,"                ","{0:.2f}".format(ocena))

            