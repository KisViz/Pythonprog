import argparse
import dataclasses
from datetime import datetime
import requests

HP_API = "https://hp-api.onrender.com/api/characters"

@dataclasses.dataclass()
class Varazslo:
    name: str
    house: str
    yearOfBirth: int

    @property
    def kor(self):
        if self.yearOfBirth and self.yearOfBirth != 0:
            return datetime.now().year - self.yearOfBirth
        else:
            return None

def filter_haz(haz: str, karakterek: list):
    if haz == "all":
        return karakterek

    uj = []
    for elem in karakterek:
        if elem.house == haz:
            uj.append(elem)
    return uj

def oreg(karakterek: list):
    legoregebb = karakterek[0]
    for elem in karakterek:
        if elem.kor > legoregebb.kor:
            legoregebb = elem
    return legoregebb

def fiatal(karakterek: list):
    legfiatalabb = karakterek[0]
    for elem in karakterek:
        if elem.kor < legfiatalabb.kor:
            legfiatalabb = elem
    return legfiatalabb

def atlag(karakterek: list):
    korok = []
    for elem in karakterek:
        if elem.kor is not None:
            korok.append(elem.kor)

    return int(sum(korok) / len(korok)) if korok else 0

def main():
    # kigyujtjuk a karakteteket
    osszes = requests.get(HP_API).json()  # jsonben elkerjeuk az apit
    # print("válasz", osszes)

    karakterek = []
    for elem in osszes:
        # kiszedjuk az eloket es azokat, akiknek van koruk megadva
        if elem.get('alive') and elem.get('yearOfBirth'):
            tmp = Varazslo(
                name = elem['name'],
                house = elem['house'],
                yearOfBirth = elem['yearOfBirth'],
            )
            karakterek.append(tmp)
    # print(karakterek)

    # osszeszedjuk az arumentumokat
    parser = argparse.ArgumentParser()
    parser.version = '1.0'
    parser.add_argument('-y', action='store_true', help='legfiatalabb')
    parser.add_argument('-o', action='store_true', help='legidosebb')
    parser.add_argument('-avg', action='store_true')
    parser.add_argument('-house', choices=['Gryffindor', 'Ravenclaw', 'Slytherin', 'all'], default='all')

    args = parser.parse_args()

    # leszurjuk a karaktereket haz szerint
    karakterek = filter_haz(args.house, karakterek)

    # sorban kiiratjuk a dolgokat
    if args.o:
        print(oreg(karakterek).name)

    if args.y:
        print(fiatal(karakterek).name)

    if args.avg:
        print(atlag(karakterek))

if __name__ == "__main__":
    main()