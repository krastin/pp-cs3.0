temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
print(temps)

temps.sort()
print(temps)

cool_temps = temps[:2]
warm_temps = temps[2:]
print(cool_temps)
print(warm_temps)

print(cool_temps + warm_temps)