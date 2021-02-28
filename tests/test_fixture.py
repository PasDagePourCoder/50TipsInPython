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
