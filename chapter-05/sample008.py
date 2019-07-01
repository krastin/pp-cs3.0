ph = float(input('Enter the pH level: '))
if ph < 7.0:
    print(ph, "is acidic.")
    print("You should be careful with that!")
elif ph > 7.0:
    print(ph, "is basic.")