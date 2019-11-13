import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# clean up in case of old executions
cur.execute('DROP TABLE PopByRegion')

# create and add records
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')

cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
#cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Japan", 100562))

con.commit()

# query
cur.execute('SELECT Region, Population FROM PopByRegion')
print(cur.fetchone())

cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
print(cur.fetchall())

cur.execute('''SELECT Region, Population FROM PopByRegion ORDER BY Population DESC''')
print(cur.fetchone())

cur.execute('SELECT Region FROM PopByRegion')
print(cur.fetchall())

cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())

cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
print(cur.fetchall())

cur.execute('''SELECT Region
            FROM PopByRegion
            WHERE Population > 1000000 AND
            Region < "L"''')
print(cur.fetchall())

# update and delete
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchone())

cur.execute('''UPDATE PopByRegion SET Population = 100600
            WHERE Region = "Japan"''')

cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchone())


cur.execute('DELETE FROM PopByRegion WHERE Region < "L"')
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())

cur.execute('INSERT INTO PopByRegion VALUES ("Mars", NULL)')

cur.execute('CREATE TABLE Test (Region TEXT NOT NULL, '
            'Population INTEGER)')
# cur.execute('INSERT INTO Test VALUES (NULL, 456789)') # this will fail

con.close()
