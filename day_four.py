'''This script solves part one and part two for day four of the Advent
of Code fun'''
import re

NAPDATA = []
with open("input_guard_naps.txt", "r") as file:
#with open("sample_naps.txt", "r") as file:
    for line in file:
        line = line.strip('\n')
        NAPDATA.append(line)
NAPDATA.sort()

ALLNAPS = []
for NAPS in NAPDATA:
    #year = re.findall(r'\d\d\d\d', NAPS)
    month = re.findall(r'\-(\d\d)\-', NAPS)
    day = re.findall(r'\-(\d\d)\s', NAPS)
    minute = re.findall(r'\:(\d\d)', NAPS)
    nap_status = re.findall(r'\]\s(\w+\s\w+)', NAPS)

    if not nap_status:
        nap_status = "begins shift"

    guard_id = (re.findall(r'\#\w*', NAPS))
    if guard_id:
        pre_guard_id = guard_id
    elif not guard_id:
        guard_id = pre_guard_id

    data = ("MD " + month[0]+ " " + day[0], minute[0], nap_status[0], guard_id[0])
    ALLNAPS.append(data)

LSTGID = [item[3] for item in ALLNAPS]
LSTGID = list(set(LSTGID))

NAPMINUTES = []
#store when a guard works by minute and how often
for gid in LSTGID:
    for i in range(0, 60, 1):
        NAPMINUTES.append([gid, i, 0])

DATE = []
TIMESLEPT = []
DAYNUMBERS = []
FLAGGED = []

POSCALC = 0
NEGCALC = 0
CALCDATA = []
X = 0
Y = 0

for gid in LSTGID:
    # pulls data by gid into matching
    #sublist matching GID
    FLAGGED = []
    matching = [s for s in ALLNAPS if gid in s]
    DAYNUMBERS = []
    if len(matching) == 1:
        pass
    else:
        for match in matching:
            if len(match) == 1:
                pass
            else:
                descrip = match[2:3]
                if descrip == (('b',)):
                    X = 0
                    Y = 0
                elif descrip == (('falls asleep',)):
                    NEGCALC = match[1:2]
                    NEGCALC = int(NEGCALC[0]) * -1
                    DAYNUMBERS.append(NEGCALC)
                    X = NEGCALC * -1
                elif descrip == (('wakes up',)):
                    POSCALC = match[1:2]
                    POSCALC = int(POSCALC[0])
                    DAYNUMBERS.append(POSCALC)
                    Y = POSCALC

                while Y > X:
                    Y = Y - 1
                    FLAGGED.append(Y)

                for sublist in NAPMINUTES:
                    if sublist[0] == gid:
                        if sublist[1] in FLAGGED:
                            nap_minute = int(sublist[2])
                            sublist[2] = 1 + nap_minute
                FLAGGED = []
        #Guard ID, Month/Day, Nap Muniute
        if (sum(DAYNUMBERS)) > 0:
            day_data = (gid, sum(DAYNUMBERS))
        CALCDATA.append(day_data)
MOSTTIME = max(CALCDATA, key=lambda X: X[1])

#This tells you the guard who napped for the most time
print(MOSTTIME)

GUARDLIST = []
for sublist in NAPMINUTES:
    if sublist[0] == MOSTTIME[0]:
        GUARDLIST.append(sublist)

#This prints out the guard, the minute, and the number of times the guard
#slept in that minute
print(max(GUARDLIST, key=lambda X: X[2]))

#Next line gives you the answer for part 2
print(max(NAPMINUTES, key=lambda X: X[2]))
