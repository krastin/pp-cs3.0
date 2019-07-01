x = False
y = True

# a. Write an expression that produces True iff both variables are True.
print((x and not y) or (y and not x))

# b. Write an expression that produces True iff x is False.
print(not x)

# c. Write an expression that produces True iff at least one of the variables is True.
print(x or y)