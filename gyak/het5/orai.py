import os
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path

@contextmanager
def change_dir(d):
    eredeti_mappa = Path.cwd()  #aktualis
    try:
        os.chdir(d)  #atmegyunk
        yield
    finally:
        os.chdir(eredeti_mappa)  #vissza

print(os.getcwd())

with change_dir("../"):
    print(os.getcwd())

print(os.getcwd())
print("-------")


def stats(a_directory):                             #valami nagy kell:(
    alap = defaultdict(lambda: {"atlagos_fajlmeret": 0, "min_fajlmeret": 99999999999999, "max_fajlmeret": 0, "fajlok_szama": 0, "osszeg": 0})

    for file in Path(a_directory).iterdir(): #bejarjuk a konyvtarat
        if file.is_file():
            kiterjesztes = file.suffix.lower().lstrip(".") or "nincs" #ne szamitson a kis es nagy betu
            meret = file.stat().st_size #adott merete

            alap[kiterjesztes]["fajlok_szama"] += 1
            alap[kiterjesztes]["osszeg"] += meret
            alap[kiterjesztes]["min_fajlmeret"] = min(alap[kiterjesztes]["min_fajlmeret"], meret) #kikeressuk az adott kiterjesztesuek koziul a lehkisebbet
            alap[kiterjesztes]["max_fajlmeret"] = max(alap[kiterjesztes]["max_fajlmeret"], meret)

    for kiterjesztes, values in alap.items(): #atlag
        values["atlagos_fajlmeret"] = values["osszeg"] // values["fajlok_szama"]
        del values["osszeg"]

    return dict(alap)

print(stats("masik_almodul"))
print("-------")

import os
import shutil


def rendez_mappa(mappa_nev):
    cica_mappa = os.path.join(mappa_nev, "cicas_dolgok")
    kutya_mappa = os.path.join(mappa_nev, "kutyas_dolgok")

    #letrehozzukoket ugy hogy ne dobjun hibat
    os.makedirs(cica_mappa, exist_ok=True)
    os.makedirs(kutya_mappa, exist_ok=True)

    #vegigmegyunk
    for fajl in os.listdir(mappa_nev):
        fajl_utvonal = os.path.join(mappa_nev, fajl)

        # Csak fájlokkal foglalkozunk
        if os.path.isfile(fajl_utvonal):
            try:
                with open(fajl_utvonal, "r", encoding="utf-8") as f:
                    tartalom = f.read()

                    if "cat" in tartalom:
                        shutil.copy(fajl_utvonal, cica_mappa)
                    elif "dog" in tartalom:
                        shutil.copy(fajl_utvonal, kutya_mappa)
            except Exception as e:
                pass
            
rendez_mappa("sajat_mappa")
