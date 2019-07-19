rat_1_weight = 1.1
rat_2_weight = 1.1

# percent of growth per week
rat_1_rate = 8
rat_2_rate = 5

rat_1_starting_weight = rat_1_weight
rat_2_starting_weight = rat_2_weight
weeks = 0

while rat_1_weight < rat_1_starting_weight * 1.25:
    weeks += 1
    rat_1_weight += (rat_1_rate * rat_1_weight) / 100
    rat_2_weight += (rat_2_rate * rat_2_weight) / 100
    print('Week: ', weeks)
    print('Rat 1: {:.2f}'.format(rat_1_weight))
print("It took {} weeks for Rat 1 to get 25% heavier".format(weeks))

# reset data for second run
weeks = 0
rat_1_weight = rat_1_starting_weight
rat_2_weight = rat_2_starting_weight

while rat_1_weight < rat_2_weight * 1.1:
    weeks += 1
    rat_1_weight += (rat_1_rate * rat_1_weight) / 100
    rat_2_weight += (rat_2_rate * rat_2_weight) / 100
    print('Week: ', weeks)
    print('Rat 1: {:.2f}'.format(rat_1_weight))
    print('Rat 2: {:.2f}'.format(rat_2_weight))
print("It took {} weeks for Rat 1 to get 10% heavier than Rat 2".format(weeks))