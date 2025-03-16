# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775
import datetime


def eltelt_ido(ora1, perc1, ora2, perc2):
    #letrehozzuk az idoket
    elso = datetime.datetime(2000, 1, 1, ora1, perc1)
    masodik = datetime.datetime(2000, 1, 1, ora2, perc2)

    #ha nem jo, akkor megforditjuk es elvileg pacek lesz
    if masodik < elso:
        elso, masodik = masodik, elso

    #es visszaadjuk
    tmp = masodik - elso
    return datetime.time(int(tmp.total_seconds() // 3600), int((tmp.total_seconds() % 3600) // 60))

import csv

def kesesek(utvonal):
    nev, legnagyobb = None, None

    try:
        with open(utvonal, 'r') as fajl:
            csvreader = csv.reader(fajl, delimiter=',')

            elso = True
            for row in csvreader:
                #a headert atugorjuk
                if elso:
                    elso = False
                    continue

                #megnezzuk az elterest
                megbeszelt = datetime.datetime.strptime(row[1].strip(), "%Y-%m-%d %H:%M:%S")
                tenyleges = datetime.datetime.strptime(row[2].strip(), "%Y-%m-%d %H:%M:%S")
                ido = tenyleges - megbeszelt

                if legnagyobb is None or legnagyobb < ido:
                    legnagyobb = ido
                    nev = row[0].strip()
    except FileNotFoundError:
        return None

    return nev

# print(kesesek("adatok.csv"))



# print("sima")
# print(eltelt_ido(1, 1, 3, 2))
# print(eltelt_ido(5, 23, 14, 9))
#
# print("nagyobb")
# print(eltelt_ido(22, 30, 1, 15))
# print(eltelt_ido(5, 43, 3, 55))
#
#
# print("azonos")
# print(eltelt_ido(10, 30, 10, 30))
# print(eltelt_ido(1, 1, 1, 1))
#
# print("kicsi")
# print(eltelt_ido(14, 59, 15, 0))
# print(eltelt_ido(3, 4, 3, 2))
#
# print("max")
# print(eltelt_ido(23, 59, 0, 0))
#
# print("max forditva")
# print(eltelt_ido(0, 0, 23, 59))

# sima
# 02:01:00
# 08:046:00
# nagyobb
# 21:15:00
# 01:48:00
# azonos
# 00:00:00
# 00:00:00
# kicsi
# 00:01:00
# 00:02:00
# max
# 23:59:00
# max forditva
# 23:59:00