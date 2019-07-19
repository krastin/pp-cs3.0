width = 7

x = 1
while x < (width+1):
    y = 1
    while y < (x+1):
        print('T', end='')
        y += 1
    print()
    x += 1

x = 1
while x < (width+1):
    y = width-x+1
    while y > 1:
        print(' ', end='')
        y -= 1
    print('T'*x)
    x += 1