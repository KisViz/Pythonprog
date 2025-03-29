import requests
import json
from dataclasses import dataclass



@dataclass
class Karakter:
    id: str
    name: str
    alternate_names: list[str]
    species: str
    gender: str
    house: str
    dateOfBirth: str
    yearOfBirth: int
    wizard: bool
    ancestry: str
    eyeColour: str
    hairColour: str
    wand: dict[str, [str]]
    patronus: str
    hogwartsStudent: bool
    hogwartsStaff: bool
    actor: str
    alternate_actors: list[str]
    alive: bool
    image: str


#api hivas
response = requests.get("https://hp-api.onrender.com/api/characters")
adatok = response.json()

#adatok tarulasa
karakterek = []
for adat in adatok:
    tmp = Karakter(
    id = adat["id"],
    name = adat["name"],
    alternate_names = adat["alternate_names"],
    species = adat["species"],
    gender = adat["gender"],
    house = adat["house"],
    dateOfBirth = adat["dateOfBirth"],
    yearOfBirth = adat["yearOfBirth"],
    wizard = adat["wizard"],
    ancestry = adat["ancestry"],
    eyeColour = adat["eyeColour"],
    hairColour = adat["hairColour"],
    wand = adat["wand"],
    patronus = adat["patronus"],
    hogwartsStudent = adat["hogwartsStudent"],
    hogwartsStaff = adat["hogwartsStaff"],
    actor = adat["actor"],
    alternate_actors = adat["alternate_actors"],
    alive = adat["alive"],
    image = adat["image"]
    )
    karakterek.append(tmp)

#hazankent
hazak = {}

for karakter in karakterek:
    if karakter.house:
        if karakter.house not in hazak:
            hazak[karakter.house] = 0
        hazak[karakter.house] += 1


#haj es szemszinek
hajszinek = {}
szemszinek = {}

for karakter in karakterek:
    if karakter.hairColour not in hajszinek:
        hajszinek[karakter.hairColour] = 0
    hajszinek[karakter.hairColour] += 1

    if karakter.eyeColour not in szemszinek:
        szemszinek[karakter.eyeColour] = 0
    szemszinek[karakter.eyeColour] += 1

#max haj es szem
legtobb_hajszin = max(hajszinek, key=hajszinek.get)
legtobb_szemszin = max(szemszinek, key=szemszinek.get)

#nem emberek
nem_emberek = []
for karakter in karakterek:
    if karakter.species.lower() != "human":
        nem_emberek.append(karakter.name)


#statisztika
with open("statisztika.txt", "w") as f:
    f.write("Hazak szerinti eloszlas:\n")
    for haz, darab in hazak.items():
        f.write(f"{haz}: {darab} fo\n")

    f.write("\nLeggyakoribb hajszin:\n")
    if legtobb_hajszin:
        f.write(f"{legtobb_hajszin[0][0]}: {legtobb_hajszin[0][1]} fo\n")

    f.write("\nLeggyakoribb szemszin:\n")
    if legtobb_szemszin:
        f.write(f"{legtobb_szemszin[0][0]}: {legtobb_szemszin[0][1]} fo\n")

    f.write("\nNem emberi karakterek:\n")
    for nev in nem_emberek:
        f.write(f"{nev}\n")

#hazak szerint
hazak_szerint = {}

for karakter in karakterek:
    if karakter.house:
        if karakter.house not in hazak_szerint:
            hazak_szerint[karakter.house] = []
    else:
        continue

    tmp = {
    "id": karakter.id,
    "name": karakter.name,
    "alternateNames": karakter.alternate_names,
    "species": karakter.species,
    "gender": karakter.gender,
    "house": karakter.house,
    "dateOfBirth": karakter.dateOfBirth,
    "yearOfBirth": karakter.yearOfBirth,
    "wizard": karakter.wizard,
    "ancestry": karakter.ancestry,
    "eyeColour": karakter.eyeColour,
    "hairColour": karakter.hairColour,
    "wand": karakter.wand,
    "patronus": karakter.patronus,
    "hogwartsStudent": karakter.hogwartsStudent,
    "hogwartsStaff": karakter.hogwartsStaff,
    "actor": karakter.actor,
    "alternate_actors": karakter.alternate_actors,
    "alive": karakter.alive,
    }
    hazak_szerint[karakter.house].append(tmp)

#kiiras
with open("hogwarts-by-house.json", "w") as f:
    json.dump(hazak_szerint, f, indent= 4)
                                #ez azert kell, hogy ne egy sorba rakja ble