import csv


def feldolgoz_csv(bemeneti_fajl, kimeneti_fajl):
    # az adatoknak
    adatok = {}
    fejlecek = []

    with open(bemeneti_fajl, 'r') as bemenet:
        olvaso = csv.DictReader(bemenet)

        # fejlec
        eredeti_fejlecek = olvaso.fieldnames
        fejlecek = ['Country/Region']

        # datumok atalakitasa
        datum_oszlopok = []
        for oszlop in eredeti_fejlecek:
            if oszlop in ['Province/State', 'Country/Region', 'Lat', 'Long']:  # ezek nem kellenek
                continue
            try:
                # masban is lehet "/" jel
                reszek = oszlop.split('/')
                if len(reszek) == 3:
                    honap, nap, ev = reszek
                    # atiras
                    uj_datum = f"20{ev}-{honap.zfill(2)}-{nap.zfill(2)}"  # hogy szepen jelenjen meg a 01 stb
                    fejlecek.append(uj_datum)
                    datum_oszlopok.append(oszlop)
            except ValueError:
                continue

        # orszagoks sorai
        for sor in olvaso:
            orszag = sor['Country/Region']

            # uj orszag, ha meg nincs benne az adatok dicctben, akkor bele rakjuk
            if orszag not in adatok:
                adatok[orszag] = {datum_oszlop: 0 for datum_oszlop in datum_oszlopok}  # alapertelmezett az 0

            # osszegzes
            for datum_oszlop in datum_oszlopok:
                try:
                    # kiolvassik a datumhoz tartozo erteket
                    ertek = sor[datum_oszlop]
                    if ertek is None or ertek.strip() == '':
                        ertek = 0
                    else:
                        ertek = int(ertek)
                except Exception:
                    ertek = 0
                adatok[orszag][datum_oszlop] += ertek  # hozzaadjuk a mar meglevohoz

    # mentes
    with open(kimeneti_fajl, 'w', newline='') as kimenet:
        iro = csv.writer(kimenet)
        iro.writerow(fejlecek)

        for orszag, ertekek in adatok.items():
            sor_adatok = [orszag]
            for datum_oszlop in datum_oszlopok:
                sor_adatok.append(ertekek[datum_oszlop])
            iro.writerow(sor_adatok)


if __name__ == "__main__":
    bemeneti_fajlnev = "../csv/nyers/time_series_covid19_confirmed_global.csv"
    # bemeneti_fajlnev = "../nyers/tests.csv" #teszteleshez
    kimeneti_fajlnev = "../csv/feldolgozott/fertozottek.csv"

    feldolgoz_csv(bemeneti_fajlnev, kimeneti_fajlnev)
    print("feldolgozás kész")
