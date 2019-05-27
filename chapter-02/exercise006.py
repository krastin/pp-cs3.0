x = 3
x += x - x
print(x)
"""
1. x references int [3]
2. x - x is calculated to be 0, this value is put into memory
3. x is set to reference the former value's memory address
"""