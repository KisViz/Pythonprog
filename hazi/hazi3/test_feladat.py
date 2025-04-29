import pytest
from feladat import Varazslo, filter_haz, oreg, fiatal, atlag

@pytest.fixture
def test_characters():
    return [
        Varazslo("Harry Potter", "Gryffindor", 1980),
        Varazslo("Hermione Granger", "Gryffindor", 1979),
        Varazslo("Draco Malfoy", "Slytherin", 1980),
        Varazslo("Luna Lovegood", "Ravenclaw", 1981)
    ]

def test_filter_all(test_characters):
    filtered = filter_haz("all", test_characters)
    assert len(filtered) == 4

def test_filter_specific_house(test_characters):
    filtered = filter_haz("Slytherin", test_characters)
    assert len(filtered) == 1
    assert filtered[0].name == "Draco Malfoy"

def test_get_oldest(test_characters):
    oldest = oreg(test_characters)
    assert oldest.name == "Hermione Granger"

def test_get_youngest(test_characters):
    youngest = fiatal(test_characters)
    assert youngest.name == "Luna Lovegood"

def test_get_average(test_characters):
    current_year = 2025
    expected_ages = [current_year - c.yearOfBirth for c in test_characters]
    expected_avg = sum(expected_ages) // len(expected_ages)
    assert atlag(test_characters) == expected_avg

def test_character_age():
    c = Varazslo("Test", "Testhouse", 2000)
    current_year = 2025
    assert c.kor == current_year - 2000

def test_character_age_none():
    c = Varazslo("NoYear", "Nowhere", 0)
    assert c.kor is None
