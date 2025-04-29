import argparse
import requests
from dataclasses import dataclass
from datetime import datetime

API_URL = "https://hp-api.onrender.com/api/characters"


@dataclass
class Character:
    name: str
    house: str
    alive: bool
    yearOfBirth: int

    def age(self) -> int | None:
        now = datetime.now().year
        if self.yearOfBirth and self.yearOfBirth != 0:
            return now - self.yearOfBirth
        else:
            return None


def alive_characters() -> list:
    response = requests.get(API_URL)
    response.raise_for_status()
    characters = []
    for c in response.json():
        if c.get('alive') and c.get('yearOfBirth'):
            characters.append(Character(
                name=c['name'],
                house=c.get('house', ''),
                alive=c['alive'],
                yearOfBirth=c['yearOfBirth']
            ))
    return characters


def filter_characters(characters: list, house: str) -> list:
    filtered_characters = []
    if house == "all":
        return characters

    for c in characters:
        if c.house == house:
            filtered_characters.append(c)
    return filtered_characters


def get_oldest(characters: list) -> Character:
    oldest = characters[0]
    for character in characters:
        if character.yearOfBirth < oldest.yearOfBirth:
            oldest = character
    return oldest


def get_youngest(characters: list) -> Character:
    youngest = characters[0]
    for character in characters:
        if character.yearOfBirth > youngest.yearOfBirth:
            youngest = character
    return youngest

def get_average(characters: list) -> float:
    ages = []
    for c in characters:
        age = c.age()
        if age is not None:
            ages.append(age)

    if len(ages) > 0:
        return int(sum(ages) / len(ages))
    else:
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.version = '1.0'
    parser.add_argument('-y', action='store_true', help='youngest')
    parser.add_argument('-o', action='store_true', help='oldest')
    parser.add_argument('-avg', action='store_true')
    parser.add_argument('-house', choices=['Gryffindor', 'Ravenclaw', 'Slytherin', 'all'], default='all')

    args = parser.parse_args()

    characters = alive_characters()
    characters = filter_characters(characters, args.house)

    if args.o:
        oldest = get_oldest(characters)
        print(f"{oldest.name}")

    if args.y:
        youngest = get_youngest(characters)
        print(f"{youngest.name}")

    if args.avg:
        avg_age = get_average(characters)
        print(f"{avg_age}")


if __name__ == "__main__":
    main()
