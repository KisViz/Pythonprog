import csv
import datetime

def nonap_statisztika():
    stat = {}
    napok = ["hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat", "vasarnap"]

    for ev in range(datetime.date.today().year - 30, datetime.date.today().year):
        if napok[ datetime.date.weekday(datetime.date(ev,3,8))] in stat:
            stat[napok[datetime.date.weekday(datetime.date(ev,3,8))]] += 1
        else:
            stat[napok[datetime.date.weekday(datetime.date(ev,3,8))]] = 1

    return stat

print(nonap_statisztika())



def pentek13(hany: int):
    szaml = 0

    for ev in range(datetime.date.today().year - hany, datetime.date.today().year):
        for honap in range(1, 13):
            szaml += 1 if datetime.date.weekday(datetime.date(ev, honap, 13)) == 4 else 0

    return szaml

print(pentek13(5))

def netflix_decade_data():
    #eredeti es cel
    forras_mappa = Path("csv_fajlok/netflix_yearly_data")
    cel_mappa = Path("csv_fajlok/netflix_decade_data")
    cel_mappa.mkdir(exist_ok=True) #ha mar letezik nem hal meg

    for file in forras_mappa.iterdir(): #bejarjuk az eredeti mappat
        #es letre hozzuk a neveket minden filehoz
        evtized = int(file.name.split("-")[1][0:3] + "0")
        uj_file = str(evtized) + "_" + str(evtized + 10) + ".csv"

        # megnyitjuk folytatosan az adott evtized filejat
        with open("csv_fajlok/netflix_decade_data/" + uj_file, "a") as csvfile:
            with open(file, "r", encoding="utf-8") as eredeti:
                #innentol meghal:(
                tized_writer = csv.writer(csvfile)
                eredeti_reader = csv.reader(eredeti)
                for row in eredeti_reader:
                    tized_writer.writerow(row)



# netflix_decade_data()

import re

def ideggorcs(szoveg: str):
    return bool(re.search(r"!![4!]*!", szoveg))

print([ideggorcs(t) for t in """Akkor nem kell!
Akkor nem kell!!!!!
Akkor nem kell!!
Akkor nem kell!!444!4!4!!!!
Akkor nem kell!!444!4!4!4!4!
""".splitlines()])


from pathlib import Path

def osszevon(mappa: Path):
    vege = Path("teljes_netflix.csv")
    forras_mappa = Path("csv_fajlok/netflix_yearly_data")


    with open(vege, 'w') as csvfile:
        for file in forras_mappa.iterdir():  # bejarjuk az eredeti mappat
            with open(file, "r") as eredeti:
                uj_writer = csv.writer(csvfile)
                eredeti_reader = csv.reader(eredeti)
                for row in eredeti_reader:
                    uj_writer.writerow(row)

Path("csv_fajlok/netflix_yearly_data")