# list to hold all frequencies used
frequency = []
x = 0

# create and populate list of all variables used to calculate frequencies
variables = []

with open("input.txt", "r") as file:
    for line in file:
        variables.append(int(line))
	
done = "False"
while done == "False":
    for i in variables [:]:
        x = x + i
        if x in frequency:
            print(x)
            done = "True"
            break
        frequency.append(x)
