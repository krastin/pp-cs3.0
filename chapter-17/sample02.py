# please run sample01 before this one

import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# cleanup from previous executions
cur.execute('DROP TABLE PopByCountry')

'''
cur.execute('CREATE TABLE PopByCountry(Region TEXT, Country TEXT, Population INTEGER)')
'''

cur.execute(''' CREATE TABLE PopByCountry(
            Region TEXT NOT NULL,
            Country TEXT NOT NULL,
            Population INTEGER NOT NULL,
            CONSTRAINT CountryKey PRIMARY KEY (Region, Country))
            ''')

cur.execute('''INSERT INTO PopByCountry VALUES("Eastern Asia", "China",
            1285238)''')

countries = [
    ("Eastern Asia", "DPR Korea", 24056),
    ("Eastern Asia", "Hong Kong (China)", 8764),
    ("Eastern Asia", "Mongolia", 3407),
    ("Eastern Asia", "Republic of Korea", 41491),
    ("Eastern Asia", "Taiwan", 1433),
    ("North America", "Bahamas", 368),
    ("North America", "Canada", 40876),
    ("North America", "Greenland", 43),
    ("North America", "Mexico", 126875),
    ("North America", "United States", 493038)
    ]

for c in countries:
    cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (c[0], c[1], c[2]))

con.commit()

cur.execute('''
            SELECT PopByRegion.Region, PopByCountry.Country
            FROM PopByRegion INNER JOIN PopByCountry
            WHERE (PopByRegion.Region = PopByCountry.Region)
            AND (PopByRegion.Population > 1000000)
            ''')
print(cur.fetchall())

cur.execute('''
            SELECT DISTINCT PopByRegion.Region
            FROM PopByRegion INNER JOIN PopByCountry
            WHERE (PopByRegion.Region = PopByCountry.Region)
            AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)
            ''')
print(cur.fetchall())

