with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()

for planet in sorted(planets):
    print(planet.strip())
