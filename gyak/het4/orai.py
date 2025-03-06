import datetime

def nonap_statisztika():
    stat = {}
    napok = ["hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat", "vasarnap"]

    #               2025-30 (= 1995) tol 2025
    for ev in range(datetime.date.today().year - 30, datetime.date.today().year):
        nap = datetime.date(ev, 3, 8).weekday() #letrehozzu a datumot es megnezzuk meliyk nap

        if nap in stat:
            stat[nap] += 1
        else:
            stat[nap] = 1

    uj = {}

    for i in range(0,7):
        uj[napok[i]] = stat[i]

    # print(uj)
    return uj

print(nonap_statisztika())


def pentek13(hany: int):
    szaml = 0
                    #ev mettol mddig
    for ev in range(datetime.datetime.today().year - hany, datetime.date.today().year):
        for honap in range(1,13): #honapokon vegig
            szaml += 1 if datetime.date(ev, honap, 13).weekday() == 4 else 0

    return szaml

print(pentek13(5))


def netflix_decade_data():
    pass


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
    if not mappa.is_dir():
        raise ValueError(f'Mappa {mappa} is not a directory')
    final = Path("teljes_netflix.csv")

    with open(final, 'w') as csvfile:
        has_reader = False
        for file in mappa.glob("*.csv"):
            text = file.read_text().splitlines()
            if not has_reader:
                csvfile.write(text[0] + "\n")
                has_reader = True

            csvfile.write("\n".join(text[1::]))

Path("csv_fajlok/netflix_yearly_data")