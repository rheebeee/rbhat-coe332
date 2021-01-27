import json
import random

num= random.randrange(0,19)

with open('animals.json', 'r') as f:
    animals = json.load(f)

print(animals['animal'][num])
