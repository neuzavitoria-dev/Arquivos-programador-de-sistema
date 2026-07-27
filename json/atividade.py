import json

animal = {}

def cadastraAnimal():
    nome =

with open("animal.json", "a") as arquivo:
    json.dump(animal, arquivo, indent=4)

