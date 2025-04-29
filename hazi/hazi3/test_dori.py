import pytest
from dori import Character, filter_characters, get_oldest, get_youngest, get_average

@pytest.fixture
def test_characters():
    return [
        Character("Harry Potter", "Gryffindor", True, 1980),
        Character("Hermione Granger", "Gryffindor", True, 1979),
        Character("Draco Malfoy", "Slytherin", True, 1980),
        Character("Luna Lovegood", "Ravenclaw", True, 1981)
    ]

def test_filter_all(test_characters):
    filtered = filter_characters(test_characters, "all")
    assert len(filtered) == 4

def test_filter_specific_house(test_characters):
    filtered = filter_characters(test_characters, "Slytherin")
    assert len(filtered) == 1
    assert filtered[0].name == "Draco Malfoy"

def test_get_oldest(test_characters):
    oldest = get_oldest(test_characters)
    assert oldest.name == "Hermione Granger"

def test_get_youngest(test_characters):
    youngest = get_youngest(test_characters)
    assert youngest.name == "Luna Lovegood"

def test_get_average(test_characters):
    current_year = 2025
    expected_ages = [current_year - c.yearOfBirth for c in test_characters]
    expected_avg = sum(expected_ages) // len(expected_ages)
    assert get_average(test_characters) == expected_avg

def test_character_age():
    c = Character("Test", "Testhouse", True, 2000)
    current_year = 2025
    assert c.age() == current_year - 2000

def test_character_age_none():
    c = Character("NoYear", "Nowhere", True, 0)
    assert c.age() is None
