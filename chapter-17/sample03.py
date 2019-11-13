# please run sample01 and sample02 before this one

import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()


cur.execute('SELECT SUM (Population) FROM PopByRegion')
print(cur.fetchone())

cur.execute('''SELECT Region, SUM (Population) FROM PopByCountry GROUP BY Region''')
print(cur.fetchall())

cur.execute('''SELECT SUM (Population) FROM PopByCountry WHERE Region = "North America"''')
print(cur.fetchall())

cur.execute('''SELECT SUM (Population) FROM PopByCountry WHERE Region = "Eastern Asia"''')
print(cur.fetchall())

cur.execute('''
            SELECT A.Country, B.Country
            FROM PopByCountry A INNER JOIN PopByCountry B
            WHERE (ABS(A.Population - B.Population) <= 1000)
            AND (A.Country != B.Country)
            ''')
print(cur.fetchall())

cur.execute('''
            SELECT DISTINCT Region
            FROM PopByCountry
            WHERE Region NOT IN
                (SELECT DISTINCT Region
                FROM PopByCountry
                WHERE (PopByCountry.Population = 8764))
            ''')
print(cur.fetchall())
