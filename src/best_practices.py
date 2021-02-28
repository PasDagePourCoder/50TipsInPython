import os
import random
import time
from typing import Dict
from dataclasses import dataclass
import numpy as np

# 1. no String, use enum
from enum import Enum
gender = 'male'  # Don't

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'

gender = Gender.MALE

# 2. List Comprehension

# Don't
number_even = []
for i in range(20):
    if i % 2 == 0:
        number_even.append(i)

# Do
number_even = [x for x in range(20) if x % 2 == 0]

# 3. Inline Operator
x = random.randint(0, 1)

# Don't
if x == 1:
    value = 15
else:
    value = 10

# Do
value = 15 if x == 1 else 10

# 4. If / Elif / Else
x = random.randint(0, 10)

# Don't
if x < 5:
    value = 15
else:
    if x < 7:
        value = 10
    else:
        value = 20

# Do
if x < 5:
    value = 15
elif x < 7:
    value = 10
else:
    value = 20

# 5. Function if if statement is too complicated

# Don't
if (x < 10 and x % 2 == 0) or (x > 12 and x % 3 == 0):
    print('yes')

# Do
def my_complex_condition(x):
    return (x < 10 and x % 2 == 0) or (x > 12 and x % 3 == 0)

if my_complex_condition(x):
    print('yes')

assert my_complex_condition(4) == True == my_complex_condition(15) == my_complex_condition(8)
assert my_complex_condition(9) == False == my_complex_condition(12) == my_complex_condition(14)

# 6. Enumerate if needed

my_list = [1, 5, 9, 13]

# Don't
for i in range(len(my_list)):
    print('The value {} is at index {}'.format(my_list[i], i))

# Do
for i, value in enumerate(my_list):
    print('The value {} is at index {}'.format(value, i))

# 7. Use PEP8

# Don't
value=15
test  =   3

# Do
value = 15
test = 3


# 8. use snake_case (except for class names)

# Don't
ExampleUsefulValue = 15

# Do
example_useful_value = 15

# 9. Don't use data or information in naming (everything is data / information in fact)

# Don't
information_about_weather_in_africa = 15
data_tuesday_schedule = 'test'

# Do
weather_in_africa = 15
tuesday_schedule = 'test'

# 10. If True == True

is_locker_open = True
# Don't
if is_locker_open == True:
    print('locker is open')

# Do
if is_locker_open:
    print('locker is open')

# 11. Typing

# Don't
def my_function(a, b):
    my_dict = dict()- if elif else
    my_dict[a] = b
    return my_dict

# Do
def my_function(a: str, b: int) -> Dict[str, int]:
    my_dict = dict()
    my_dict[a] = b
    return my_dict


# 12. Use _ if variable is not used

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Don't
list_odd = [value for key, value in my_dict.items() if value % 2 != 1]

# Do  (example here, use my_dict.values() otherwise)
list_odd = [value for _, value in my_dict.items() if value % 2 != 1]

# 13. Use @dataclass if you're using few methods

# Don't
class Person():
    name: str
    gender: Gender
    age: int

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

# Do
@dataclass(frozen=True)
class Person():
    name: str
    gender: Gender
    age: int

# 14. Use docstring correctly

# Don't
def convert_seconds_to_hour(seconds: int) -> float:
    """This function convert a number of seconds (which is an integer) qnd returns a float which corresponds to the
    hours."""
    return seconds / 3600

# Do (numpy docstring or whatever, Google, Python, etc...)
def convert_seconds_to_hour(seconds: int) -> float:
    """
    Convert a number of seconds into hours.

    Parameters
    ----------
    seconds : int
        The number of seconds.

    Returns
    -------
    float
        The number in hours.
    """
    return seconds / 3600

# 15. Use of Counter object to count

from collections import Counter
z = ['banana', 'apple', 'banana', 'apple', 'kiwi', 'apple']
Counter(z)
# Counter({'apple': 3, 'banana': 2, 'kiwi': 1})

# 16. Use of set to get unique values

my_list = ['cat', 'rat', 'dragon', 'dragon', 'cat', 'ox']
list(set(my_list))
# ['cat', 'dragon', 'ox', 'rat']

# 17. Use isort to sort your imports

# Don't
from enum import Enum

import os
from typing import Dict

import random

# Do
import os
import random

from enum import Enum
from typing import Dict

# 18. You can use isinstance() to check if same object

@dataclass
class Animal:
    name: str
    age: int

test = Animal('milou', age=15)
if isinstance(test, Animal):
    print('This is an animal')

# 19. Use lru_cache for complex functions that you call often
from functools import lru_cache

@lru_cache
def my_heavy_computation(a):
    time.sleep(5)
    return a * 15

result_1 = my_heavy_computation(2)  # Wait 5 seconds
result_2 = my_heavy_computation(2)  # Instantly as result is cached

# 20. Pip freeze requirements.txt

# 21. Add a README.md to your project

# 22. .gitignore

# 23. Use of Python .dotenv
import os
SECRET_KEY = os.getenv("EMAIL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

# 24. Use logger to store message

# Don't
print('The database is now set up.')

# Do
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('The database is now set up.')  # will not print anything

# 25. **kwargs and **args

def generate_pokemon(level=None, name=None, color=None, element_type=None):
    my_pokemon = {'level': level, 'name': name, 'color': color, 'element_type': element_type}
    return my_pokemon

def generate_pokemon_variant(**kwargs):
    d = dict()
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))
        d[key] = value
    return d

pikachu = generate_pokemon_variant(level=15)
raichu = generate_pokemon(level=25, name='raichu', color='yellow')  # ...

# 26. Use pandas to manipulate dataframe

import pandas as pd
df = pd.read_csv('my_example.csv')

# 27. Define a filter mask or use the filter function when possible
df = pd.DataFrame({'color': ['blue', 'yellow', 'yellow'], 'level': [20, 30, 70]})
df_filtered = df[(df['color'] == 'yellow') & (df['level'] <= 50)]

df_filtered = df.query("color == 'yellow'").query('level < 50')

# 28. Don't loop over dataframe

# Don't
for row in df.iterrows():
    df['level'] = df['level'] * 5

# Do
df['level'] = df.apply(lambda row: row['level'] * 5, axis=1)

# 29. Initialize a list easily

# Don't
my_example = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple']

# Do
my_example = ['apple'] * 6

# 30. Multiple predicates

age_person = 25
# Don't
if 18 < age_person and age_person < 30:
    print('Hello')

# Do
if 18 < age_person < 30:
    print('hello')

# 31. For if / else loop
my_list = ['luigi', 'peach', 'toad', 'wario']
for x in my_list:
    if x == 'mario':
        print('mario found')
else:
    print('where is mario ?')

# 32. Using try catch

try:
    print(x)  # Variable not existing
except:
    print("An exception occurred")

# 33. Raise value in case you want to stop it

 x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# 34. Use of break in for loop

my_list = ['luffy', 'zoro', 'sanji', 'nami']

for x in my_list:
    if x == 'sanji':
        print('sanji found')
        break  # Stop the iteration in the loop

# 35. Use of continue in for loop

my_random_list = [18, 33, 15, 56, 89]

# Don't
for x in my_random_list:
    if x > 50:
        result = x * 2
        # Others instructions...

# Do
for x in my_random_list:
    if x <= 50:
        continue
    result = x * 50
    # Others instructions...

# 36. Use @decorator

def hello(func):
    def inner(name_person):
        print("Hello ")
        func(name_person)

    return inner

@hello
def name(name_person):
    print(name_person)


name('Peter')
# Hello Peter

# 37. Define a custom type
from typing import  TypeVar, Dict


Name = TypeVar('Name', str, bytes)
Level = TypeVar('Level', int, bytes)

dict_character = {'naruto': 18, 'sasuke': 24, 'sakura': 23, 'kakashi': 32}

def print_max_level(d: Dict[Name, Level]) -> Level:
    return max(d.values())

level_max = print_max_level(dict_character)

# 38. Use Pickle to save and load object (and use them in testing)

import pickle

example = Person(name='babar', gender=Gender.MALE, age=18)

with open('filename.pickle', 'wb') as handle:
    pickle.dump(example, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    example_pickled = pickle.load(handle)

example == example_pickled  # True

# 39. Return at beginning

# Don't
def complex_computation(a: float, b: float):
    if a >= 10:
        c = a * b * 56.5656
        # Lots of lines...
        return c
    return a

# Do (easier to read)
def complex_computation(a: float, b: float):
    if a < 10:
        return a
    c = a * b * 56.5656
    # Lots of lines...
    return c

# 40. Using zip for looping over two lists

countries = ['France', 'Germany', 'Canada']
capitals = ['Paris', 'Berlin', 'Ottawa']
for country, capital in zip(countries,capitals):
    print('The capital of {} is {}'.format(country, capital))

# 41. Using f-strings can help sometimes

name = 'Ace'
age = 23
print('Hello, my name is', name, 'and my age is', age)
print(f"Hello, my name is {name} and my age is {age}.")

# 42. Create ID easily

import uuid

my_id = uuid.uuid4()

print('Your UUID is: ' + str(my_id))

# 43. Use mypy for static type checking

# pip install mypy
# mypy src

# 44. Organize your folder structure

# https://github.com/navdeep-G/samplemod

# README.rst
# LICENSE
# setup.py
# requirements.txt
# sample/__init__.py
# sample/core.py
# sample/helpers.py
# docs/conf.py
# docs/index.rst
# tests/test_basic.py
# tests/test_advanced.py

# 45. Python Easters Eggs

# import antigravity
# import this

# Hope you enjoy it !

# 46. What is yours ?

