# Tesztelés

Ezek a futtatható kódok Windows rendszeren működnek.
Linuxon a ```python``` helyett ```python3```-at, a ```pip``` helyett ```pip3```-at kell használni.

## Első lépések:
- ```pip install pytest``` : telepítsük a pytest csomagot
- ```pip install rich``` : telepítsük a rich csomagot (mert kéri a chess projekt)
#### vagy
- ```pip install -r requirements.txt``` : telepítsük a requirements.txt fájlban szereplő csomagokat

## Tesztelés:

### ```python -m pytest``` paranccsal futtathatjuk a teszteket

ez megkeresi az összes olyan fájlt aminek a neve ```test_*.py``` és ```*_test.py``` és azokban a ```test_``` prefixszel ellátott függvényeket futtatja le

### ```python -m pytest test_main.py``` paranccsal egy adott fájl tesztjeit futtathatunk

## megpiszkálandó dolgok aka elhasaló tesztek:

### test_figures.py:
- test_valid_move_rook_invalid_cannot_capture_self() : line 44 [is False]
- - legyen ```is True``` és lefut

### test_eger.py:
- mindenhol meg kell cserélni a kor és nev adattagokat a példányosításoknál

### Eger.py:
- átírni az Eger osztályt konstruktor default értékekkel, mert nincs operation overloading
- - A Java-ban működő operation overloading Pythonban másohgy néz ki, ezért javítani kell az osztályt



### Teszt opciók:
- ```python -m pytest``` : az összes tesztet lefuttatja
- ```python -m pytest -v``` : verbose, részletesebb kimenet
- ```python -m pytest -k test_main``` : megkeresi a ```test_main```-t tartalmazó fájlokat és abban a mappában lefuttatja a teszt szkripteket (main_test, test_main)
- ```python -m pytest -k test_main -v``` : csak a test_main nevű teszteket futtatja le (main_test, test_main) és részletesebb kimenet
- ```python -m pytest -k test_main -v -x``` : csak a test_main nevű teszteket futtatja le (main_test, test_main) és részletesebb kimenet, de ha egy teszt hibás, akkor megáll
- ```python -m pytest -k test_main -v -x --maxfail=2``` : csak a test_main nevű teszteket futtatja le (main_test, test_main) és részletesebb kimenet, de ha kettőnél több teszt hibás, akkor megáll

### Tesztelés mappában:
- ```python -m pytest test/``` : csak a tests mappában lévő teszteket futtatja le
- ```python -m pytest test/ -v``` : csak a tests mappában lévő teszteket futtatja le és részletesebb kimenet
- ```python -m pytest test/ -k test_main``` : csak a tests mappában lévő test_main nevű teszteket futtatja le (main_test, test_main)
- - nem fut le, mert a test mappában nincs ilyen fájl
- ```python -m pytest test/test_macska_eger/``` : csak a test_macska_eger nevű mappán belüli teszteket futtatja le
- ```python -m pytest test/test_macska_eger/ -v``` : a test_macska_eger nevű mappán belüli teszteket futtatja le és részletesebb kimenet
- ```python -m pytest test/test_macska_eger/ -k test_eger.py``` : test_macska_eger/test_eger.py tesztjeit futtatja le
- ```python -m pytest test/test_macska_eger/ -k test_eger.py -v``` : test_macska_eger/test_eger.py tesztjeit futtatja + részletesebb output
- ```python -m pytest test/test_macska_eger/ -k test_macska.py``` : test_macska_eger/test_macska.py tesztjeit futtatja le
- ```python -m pytest test/test_macska_eger/ -k test_macska.py -v``` : test_macska_eger/test_macska.py tesztjeit futtatja + részletesebb output



### Tesztelés mappában, de a fájlok nevében keresve:
- ```python -m pytest -k test_macska.py```
- ```python -m pytest -k test_macska.py -v```


- ```python -m pytest -k test_eger```
- ```python -m pytest -k test_eger -v```
- ```python -m pytest -k test_macska```
- ```python -m pytest -k test_macska -v```
- - lefutnak a test_eger.py, test_macska.py és a test_random.py tesztek, mert azt találta meg, hogy a test_macska melyik mappában van
- ```python -m pytest -k macska_teszt```
- - nem fut le, mert nincs ilyen teszt vagy fájl sehol