print(2 +
3)

print(2 + \
    3)

room_temperature = 20
cooking_temperature_f = 350
oven_heating_rate_c = 20
oven_heating_time = (
    ((cooking_temperature_f -32) * 5 / 9) - room_temperature) / \
    oven_heating_rate_c

print(oven_heating_time)

# other way around

oven_heating_time = (
    ((cooking_temperature_f - 32) * 5 / 9) - room_temperature) / \
    oven_heating_rate_c

oven_heating_time = (
    ((cooking_temperature_f - 32) * 5 / 9) -
    room_temperature) / \
    oven_heating_rate_c

room_temperature = 20
cooking_temperature_f = 350
cooking_temperature_c = (cooking_temperature_f - 32) * 5 / 9
oven_heating_rate_c = 20
oven_heating_time = (cooking_temperature_c - room_temperature) / \
    oven_heating_rate_c
print(oven_heating_time)

