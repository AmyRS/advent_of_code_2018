import collections
from collections import Counter

boxid = []
with open("input_boxID.txt", "r") as file:
    for line in file:
        boxid.append(line)
    
threes = 0
twos = 0

for string in boxid:
    letterCounts = collections.Counter(string)
    for letter in letterCounts:
        if letterCounts[letter] == 3:
            threes = threes + 1
            break
    for letter in letterCounts:
        if letterCounts[letter] == 2:
            twos = twos + 1
            break

print (threes * twos)
