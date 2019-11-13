import sqlite3

con = sqlite3.connect('census.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Density')

cur.execute('CREATE TABLE Density(Name TEXT, Population INTEGER, Area REAL)')

data = [
    ('Newfoundland and Labrador', 512930, 370501.69),
    ('Prince Edward Island', 135294, 5684.39),
    ('Nova Scotia', 908007, 52917.43),
    ('New Brunswick', 729498, 71355.67),
    ('Quebec', 7237479, 1357743.08),
    ('Ontario', 11410046, 907655.59),
    ('Manitoba', 1119583, 551937.87),
    ('Saskatchewan', 978933, 586561.35),
    ('Alberta', 2974807, 639987.12),
    ('British Columbia', 3907738, 926492.48),
    ('Yukon Territory', 28674, 474706.97),
    ('Northwest Territories', 37360, 1141108.37),
    ('Nunavut', 26745, 1925460.18)
]

for row in data:
    cur.execute('INSERT INTO Density VALUES (?, ?, ?)', (row[0], row[1], row[2]))

con.commit()

# Retrieves the contents of the table
cur.execute('SELECT * FROM Density') 
print(cur.fetchall())

# Retrieves the populations
cur.execute('SELECT Population FROM Density') 
print(cur.fetchall())

# Retrieves the provinces that have populations of less than one million
cur.execute('SELECT Name FROM Density WHERE Population < 1000000')
print(cur.fetchall())

# Retrieves the provinces that have populations of less than one million or greater than five million
cur.execute('SELECT Name FROM Density WHERE Population < 1000000 OR Population > 5000000')
print(cur.fetchall())

# Retrieves the provinces that do not have populations of less than one million or greater than five million
cur.execute('SELECT Name FROM Density WHERE Name NOT IN (SELECT Name FROM Density WHERE Population < 1000000 OR Population > 5000000)')
print(cur.fetchall())

# Retrieves the populations of provinces that have a land area greater than 200,000 square kilometers
cur.execute('SELECT Population FROM Density WHERE Area > 200000') 
print(cur.fetchall())

# Retrieves the provinces along with their population densities (population divided by land area)
cur.execute('SELECT Name, (Population / Area) AS Density FROM Density') 
print(cur.fetchall())