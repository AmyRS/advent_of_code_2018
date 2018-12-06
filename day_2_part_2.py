inputdata = open("input_boxID.txt", "r")
boxid = []

with open("input_boxID.txt", "r") as file:
    for line in file:
        boxid.append(line)
    
import jellyfish
import difflib
from difflib import SequenceMatcher

possiblematches = []

for item in boxid:
    testing = item
    for item in boxid:
        if jellyfish.levenshtein_distance(testing, item) == 1:
            possiblematches.append(testing)
possiblematches

import difflib
from difflib import SequenceMatcher
matched = SequenceMatcher(None, possiblematches[0], possiblematches[1]).get_matching_blocks()

for match in matched:
    print (possiblematches[0][match.a:match.a+match.size])
