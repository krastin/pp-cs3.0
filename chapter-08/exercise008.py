rat_1 = [1,2,3,4,5,6,7,8,9,10]
rat_2 = [11,12,13,14,15,16,17,18,19,20]

if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1.")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")

if (rat_1[0] > rat_2[0]) and (rat_1[9] > rat_2[9]):
    print("Rat 1 remained heavier than Rat 2.")
elif (rat_1[0] > rat_2[0]) and (rat_1[9] < rat_2[9]):
    print("Rat 2 became heavier than Rat 1.")

print('and now, nested')

if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1.")
    if rat_1[9] > rat_2[9]:
        print("Rat 1 remained heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")
