'''Code for day five of Advent of Code'''
import re
import string

with open("input_polymer.txt", "r") as file:
    for line in file:
        POLYMER = line

def reactions(polymer, complete):
    '''Removes items from polymer that meet criteria'''
    count = 0
    complete = False
    remove1 = re.findall(r'([a-z][A-Z]){1}', polymer)
    remove2 = re.findall(r'([A-Z][a-z]{1})', polymer)
    remove = remove1 + remove2
    for thing in remove:
        if (thing[0].upper()) == (thing[1].upper()):
            new = polymer.replace(thing, "", 1)
            polymer = new
            count = count + 1
            return polymer, complete
            break
    if count == 0:
        complete = True
        return polymer, complete

COMPLETE = False
while COMPLETE == False:
    POLYMER, COMPLETE = reactions(POLYMER, COMPLETE)
SAVE = POLYMER

POLYMER = POLYMER.strip()

POLYMER = SAVE

## Part Two

def remove_unit_type(polymer, unit):
    '''test units for likeness'''
    polymer = polymer.replace(unit.upper(), "")
    polymer = polymer.replace(unit.lower(), "")
    return polymer

ALLUNITS = string.ascii_lowercase
TESTS = []

for item in ALLUNITS:
    POLYMER = SAVE
    POLYMER = remove_unit_type(POLYMER, item)
    COMPLETE = False
    while COMPLETE == False:
        POLYMER, COMPLETE = reactions(POLYMER, COMPLETE)
    POLYMER = POLYMER.strip()
    X = len(POLYMER)
    if X > 0:
        answer = (item, len(POLYMER))
        TESTS.append(answer)

min(TESTS, key=lambda x: x[1])
