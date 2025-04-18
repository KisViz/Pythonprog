import tempfile #egy ideiglenes konyvtarat letrehoz, ami automatikusan torlodik is
import os
import csv
from src.feldolgozo import feldolgoz_csv


"""
A tempfile-t ismertem már, de szükség volt utánanézésre,
https://www.geeksforgeeks.org/create-temporary-files-and-directories-using-python-tempfile/
Hála az égnek kevesebb ai
"""


def test_feldolgoz_csv():

    #tesztadatok
    nyers_csv = """Province/State,Country/Region,Lat,Long,1/22/20,1/23/20
a,CountryA,0,0,1,2
b,CountryA,0,0,3,4
,CountryB,0,0,5,6
"""
    #azonos orszag osszevonasat is nezzuk 1 + 3 = 4 es 2 + 4 = 6

    #letrejon a tmpdir
    with tempfile.TemporaryDirectory() as tmpdir:
        bemeneti_utvonal = os.path.join(tmpdir, "input.csv")
        kimeneti_utvonal = os.path.join(tmpdir, "output.csv")

        #beleirjuk az adarokat
        with open(bemeneti_utvonal, "w", newline="") as f:
            f.write(nyers_csv)

        #meghivjuk a fuggvenyut
        feldolgoz_csv(bemeneti_utvonal, kimeneti_utvonal)

        #kiolvassuk a kimentete
        with open(kimeneti_utvonal, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)


        expected = [
            ['Country/Region', '2020-01-22', '2020-01-23'],
            ['CountryA', '4', '6'],
            ['CountryB', '5', '6']
        ]

        #ellenorizzuk
        assert rows == expected
