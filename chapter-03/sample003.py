def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

print(quadratic(2, 3, 4, 0.5))
print(quadratic(2, 3, 4, 1.5))

print(quadratic(2, 3, 4, 1.3))

def f(x):
    x = 2 * x
    return x

x = 1
x = f(x + 1) + f(x + 2)
print(x)

