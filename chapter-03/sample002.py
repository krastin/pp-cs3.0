# help(id)
print(id(9))
print(id(23.1))
shoe_size = 8.5
print(id(shoe_size))
fahrenheit = 77.7
print(id(fahrenheit))

print(id(abs))
print(id(round))

i = 3
j = 3
k = 4 - 1
print(id(i))
print(id(j))
print(id(k))

i = 30000000000
j = 30000000000
print(id(i))
print(id(j))

f = 0.0
j = 0.0
print(id(f))
print(id(j))

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(convert_to_celsius(80))

