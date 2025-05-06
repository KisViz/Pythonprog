from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dataclasses import dataclass
from collections import defaultdict
from bs4 import BeautifulSoup

@dataclass
class EvadAdat:
    evad: str
    epizodok_szama: int

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def main():
    driver.get("https://en.wikipedia.org/wiki/Outer_Banks_(TV_series)")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    cimsor = soup.find(id="Episodes")
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
    print(f"Összes epizód: {ossz_epizod}")

    evad_szotar = defaultdict(int)
    for adat in evad_lista:
        evad_szotar[adat.evad] = adat.epizodok_szama

    driver.quit()

if __name__ == '__main__':
    main()
