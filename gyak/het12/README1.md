# Pytest - Unit Test

## conftest.py

- A ```conftest.py``` fájl a pytest konfigurálásra szolgál
- A fájlban található fixture függvényeket a tesztesetekben használhatjuk ```@pytest.fixture``` dekorátorral
- Automatikusan betöltődik a pytest által, nem kell importálni (bárhol eléred a függvényeket)
- A fájlban található függvényeket a tesztesetekben használhatjuk

## Seed freezing 

- Hasznos lehet, ha a tesztelendő kódunk random számokat használ
- A seed-et a ```pytest``` futtatásakor megadhatjuk, így a tesztelés minden alkalommal ugyanazzal a seed-el fog futni
- A seed eredményeként a random számok előre megjósolhatóak lesznek (nem lesznek randomok)
- ```random.seed(42)``` - a seed értékének beállítása
- Ez **nem** jelenti azt, hogy a random szám ennyi lesz, csak egy szám, aminek szerepe van a generálásban

## Parametrized test

- A tesztesetek paraméterezhetőek


- A teszteseteket a ```@pytest.mark.parametrize``` dekorátorral paraméterezhetjük, ha több inputon akarunk tesztelni
- Ez azért jó, mert nem kell feltétlenül több tesztesetet írni, ha ugyanazt a tesztelést több inputtal szeretnénk tesztelni (például több edge case teszt egyszerre)


- Használhatjuk a ```@pytest.mark.skip``` dekorátort, ha egy tesztesetet nem akarunk futtatni
- Ez akkor hasznos, ha egy teszteset vagy a tesztelendó kód még nincs kész, de nem akarjuk törölni a tesztesetet, mert kelleni fog


- Használhatjuk a ```@pytest.mark.xfail``` dekorátort, ha egy tesztesetet futtatni akarunk, de tudjuk, hogy hibás lesz
- Ez akkor hasznos, ha tudjuk, hogy a teszteset hibás, de még nem tudjuk vagy nem akarjuk megjavítani
  - Különböző kimenetet ad, ha az eremdény helyes vagy hibás (```xpass``` vagy ```xfailed```)

## Coverage

- A tesztek lefedettségét mérhetjük a ```pytest-cov``` csomaggal
- Telepítés: ```pip install pytest-cov```
- Futtatás: ```pytest --cov=test/```: lefuttatja a teszteket és megmutatja a ```test/``` mappán belüli kódok lefedettségét
- ```pytest --cov=test_user```: lefuttatja az összes tesztet, amit talál, de csak a test_user.py lefedettségét nézi meg
- ```pytest --cov=test/ --cov-report=html```: készít egy html riportot a kódok lefedettségéről

**A lefedettség nem garantálja a minőséget, egy rossz kód is lehet 100%-os lefedettségű!**