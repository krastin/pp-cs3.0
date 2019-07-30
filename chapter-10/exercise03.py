# read in reverse
with open('alkaline_metals.txt', 'r') as inputfile:
    for line in reversed(inputfile.readlines()):
        print(line)
