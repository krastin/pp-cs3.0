alkaline_earth_metals = [
    [4, 9.012],
    [12, 24.305],
    [20, 40.078],
    [38, 87.62],
    [56, 137.327],
    [88, 226]
]

number_and_weight = []

for metal in alkaline_earth_metals:
    for metal_data in metal:
        print(metal_data)
        number_and_weight.append(metal_data)

print(number_and_weight)