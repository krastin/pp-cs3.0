width = 7
for x in range(1, width+1):
    for y in range(width-x+1, 1, -1):
        print(' ', end='')
    print('T'*x)