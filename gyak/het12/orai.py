import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

URL = r"https://en.wikipedia.org/wiki/Prison_Break"


@dataclass
class EvadAdat:
    evad: str
    epizodok_szama: int


def main():
    valasz = requests.get(URL)
    leves = BeautifulSoup(valasz.text, "html.parser")
    print("Összes kép az oldalon:", len(leves.find_all("img")))
    cimsor = leves.find(id="Series_overview")
    evad_lista = []

    if cimsor:
        tabla = cimsor.find_next("table", class_="wikitable")
        sorok = tabla.find_all("tr")[1:]
        for sor in sorok:
            oszlopok = sor.find_all(["th", "td"])
            if len(oszlopok) >= 2:
                evad_szoveg = oszlopok[0].get_text(strip=True)
                epizod_szoveg = oszlopok[1].get_text(strip=True)
                try:
                    epizodok_szama = int(epizod_szoveg)
                    evad_lista.append(EvadAdat(evad=evad_szoveg, epizodok_szama=epizodok_szama))
                except ValueError:
                    continue

    for adat in evad_lista:
        print(f"{adat.evad}: {adat.epizodok_szama} epizód")

    ossz_epizod = 0
    for adat in evad_lista:
        ossz_epizod += adat.epizodok_szama

    print("Összes epizód:", ossz_epizod)


if __name__ == '__main__':
    main()
