# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

from abc import ABC, abstractmethod

class Labbeli(ABC):

    # def __init__(self, viselheto): #property kel nem adattag:(((((
    #     self.viselheto = viselheto

    @property
    @abstractmethod #igy nem peldanyosithato
    def viselheto(self):
        pass

    def menosegi_faktor(self):
        return 0

    # @viselheto.setter #test
    # def viselheto(self, value):
    #     self._viselheto = value

# labbeli = Labbeli(True)

class Cipo(Labbeli):
    def __init__(self, marka: str, szin: str):
        # super().__init__() #nem kell!!!!!!!
        self.marka = marka
        self.szin = szin
        self.kopottsag = 0

    @property
    def viselheto(self):
        return self.kopottsag < 10

    def menosegi_faktor(self):
        return (len(self.marka) + len(self.szin)) // 2

    def visel(self):
        self.kopottsag += 1

    def is_cipo_viselheto(self):
        return self.kopottsag < 10

    # def __str__(self):
    #     return f"{self.marka}, {self.szin}, {self.kopottsag}"

# cipo = Cipo("Nike", "fekete")
# print(cipo)
# cipo.visel()
# print(cipo)
# print(cipo.menosegi_faktor())

class Converse(Cipo):
    def __init__(self, szin: str):
        super().__init__("Converse", szin)

    def menosegi_faktor(self):
        return super().menosegi_faktor() + 5

# converse_cipo = Converse("piros") #converse 8 hosszu, prios 5 hosszu
# print(converse_cipo)
# print("minosegi faktor", converse_cipo.menosegi_faktor()) # (13 // 2) + 5

class Csizma(Labbeli):
    def __init__(self, szar_magassag: int):
        # super().__init__() #itt sem:(!!!!!!
        self.szar_magassag = szar_magassag
        self.lyukas = False

    def hasznal(self, ido: int):
            if ido > 100:
                self.lyukas = True

    @property
    def viselheto(self):
        return not self.lyukas

    def is_csizma_viselheto(self):
        return not self.lyukas

    # def __str__(self):
    #     return f"{self.szar_magassag}, {self.lyukas}"

# csizma = Csizma(40)
# print(csizma)
# print("viselheto:", csizma.viselheto)
# csizma.hasznal(20)
# print(csizma)
# csizma.hasznal(120)
# print(csizma)
# csizma.hasznal(20)
# print(csizma)
# print("viselheto:", csizma.viselheto)

class HelloKittyCsizma(Cipo, Csizma):
    def __init__(self, szin: str):
        Csizma.__init__(self, 25)
        Cipo.__init__(self,"Hello Kitty csizma", szin)

    @property
    def viselheto(self):
        return Csizma.is_csizma_viselheto(self) and Cipo.is_cipo_viselheto(self)
        # return (not self.lyukas) and (self.kopottsag < 10)

    # def __str__(self):
    #     return f"{self.marka} csizma ({self.szin}, szar: {self.szar_magassag} cm, kopottsag: {self.kopottsag}, lyukas: {self.lyukas})"

# kitty = HelloKittyCsizma("rozsaszin")
# print(kitty)
# print(kitty.viselheto)

# kitty.visel()
# print(kitty)
# print(kitty.viselheto) #meg mindig hordhato
# kitty.visel()
# kitty.visel()
# kitty.visel()
# kitty.visel()
# kitty.visel()
# kitty.visel()
# kitty.visel()
# kitty.visel()
# kitty.visel()
# print(kitty)
# print(kitty.viselheto) #nem hordhato
# kitty.hasznal(150) #likas
# print(kitty)
# print(kitty.viselheto) #nem hordhato
