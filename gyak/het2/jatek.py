import random


class Kartya():
    def __init__(self, szin, ertek):
        self.szin = szin
        self.ertek = ertek

    def __repr__(self):
        return f"{self.szin} {self.ertek}"

class Pakli():
    def __init__(self):
        szinek = ["pikk", "kőr", "káró", "treff"]
        ertekek = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        self.kartyak = []
        for szin in szinek:
            for ertek in ertekek:
                self.kartyak.append(Kartya(szin, ertek))

    def __str__(self):
        return str(self.kartyak)

    def keveres(self):
        if len(self.kartyak) != 52:
            raise ValueError("Megkezdett pakli nem keverhető")

        random.shuffle(self.kartyak)
        return self

    def huzas(self):
        if len(self.kartyak) == 0:
            raise ValueError("Nincs már kártyád:(")
        return self.kartyak.pop()

uj = Pakli()
print(uj.kartyak)
uj.keveres().keveres()
print(uj.huzas())
# uj.keveres() #van error:D
for i in range(0,51):
    uj.huzas()
# uj.huzas() #itt is