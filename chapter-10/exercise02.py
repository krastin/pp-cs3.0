list_of_lists = []

with open('alkaline_metals.txt', 'r') as inputfile:
    for line in inputfile.readlines():
        list_of_lists.append(line.split())

print(list_of_lists)