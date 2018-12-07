'''This code is for Day three part one of the Advent of Code problems'''
import re
from collections import namedtuple
from shapely.ops import cascaded_union
from shapely.geometry import Polygon, MultiPolygon

CLAIMTXT = []
with open("input_claims.txt", "r") as file:
    for line in file:
        CLAIMTXT.append(line)
Claim = namedtuple('Claim', 'a b c d')
CLAIMS = []

# Pull data apart from input file for future calcs.

for claimtx in CLAIMTXT:
    claimID = (re.findall(r'(?<=#)\d*', claimtx))
    A1 = (re.findall(r'(?<=@ )\d*', claimtx))
    B1 = (re.findall(r'(?<=,)\d*', claimtx))
    C1 = (re.findall(r'(?<=: )\d*', claimtx))
    D1 = (re.findall(r'(?<=x)\d*', claimtx))
    CLAIMS.append([A1, B1, C1, D1])

A1 = [item[0] for item in CLAIMS]
B1 = [item[1] for item in CLAIMS]
C1 = [item[2] for item in CLAIMS]
D1 = [item[3] for item in CLAIMS]

def polyshapes(corner_a, corner_b, corner_c, corner_d):
    '''This function converts rectangle location data into a format we can
    use later'''
    left, top, right, bottom = sum(corner_a), sum(corner_b),\
    sum(corner_a+corner_c), sum(corner_d+corner_b)
    return left, top, right, bottom

CORNERS = []
CLAIMS = []
RECTANGLES = []

A2 = [list(map(int, x)) for x in A1]
B2 = [list(map(int, x)) for x in B1]
C2 = [list(map(int, x)) for x in C1]
D2 = [list(map(int, x)) for x in D1]

POLYS = []
for i in range(len(A1)):
    #creates polygons after changing format of input
    CORNERS = (polyshapes(A2[i], B2[i], C2[i], D2[i]))
    POLYS.append(Polygon([(CORNERS[0], CORNERS[3]), (CORNERS[2], CORNERS[3]),\
    (CORNERS[2], CORNERS[1]), (CORNERS[0], CORNERS[1])]))

POLYMULTI = []

for ITEM_POLY in POLYS:
    compare = ITEM_POLY
    for ITEM_POL in POLYS:
        if compare == ITEM_POL:
            break
        elif ITEM_POL.intersects(compare) is True:
            overlap = ITEM_POL.intersection(compare)
            if overlap.area > 0:
                POLYMULTI.append(overlap)
                #print(overlap.area)

FINALPOL = MultiPolygon(POLYMULTI)
print(cascaded_union(FINALPOL))
 