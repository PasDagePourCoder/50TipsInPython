

# 1. Use Pytest to unittests your functions

import pytest
def convert_fahrenheit_to_celsius(fahrenheit: float):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)

def test_fahrenheit_to_celsius():
    expected = 26.67
    assert convert_fahrenheit_to_celsius(80) == expected

# 2. Use mark.parametrize

@pytest.mark.parametrize("fahrenheit, expected_celsius",
                         [(80, 26.67), (50, 10), (0, -17.78)])
def test_fahrenheit_to_celsius(fahrenheit, expected_celsius):
    result = convert_fahrenheit_to_celsius(fahrenheit)
    assert result == expected_celsius

# 3. Use Fixtures

import pytest


class Person:

    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

@pytest.fixture
def person_male():
    yield Person("John", 36, 'male', 'actor')


@pytest.fixture
def person_female():
    yield Person("Marie", 24, 'female', 'actress')


def test_age(person_male):
    assert isinstance(person_male.age, int)


def test_occupation_gender(person_male, person_female):
    assert person_male.occupation == 'actor'
    assert person_female.occupation == 'actress'

# 4. Use MagicMock