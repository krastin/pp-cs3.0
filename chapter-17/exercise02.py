# please run exercise01.py before running this one

import sqlite3

con = sqlite3.connect('census.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Capitals')

cur.execute('CREATE TABLE Capitals(Name TEXT, Capital TEXT, Population INTEGER)')

data = [
    ('Newfoundland and Labrador', "St. John’s", 172918),
    ('Prince Edward Island', 'Charlottetown', 58358),
    ('Nova Scotia', 'Halifax', 359183),
    ('New Brunswick', 'Fredericton', 81346),
    ('Quebec', 'Quebec City', 682757),
    ('Ontario', 'Toronto', 4682897),
    ('Manitoba', 'Winnipeg', 671274),
    ('Saskatchewan', 'Regina', 192800),
    ('Alberta', 'Edmonton', 937845),
    ('British Columbia', 'Victoria', 311902),
    ('Yukon Territory', 'Whitehorse', 21405),
    ('Northwest Territories', 'Yellowknife', 16541),
    ('Nunavut', 'Iqaluit', 5236)
]

for row in data:
    cur.execute('INSERT INTO Capitals VALUES (?, ?, ?)', (row[0], row[1], row[2]))

con.commit()

# Retrieve the contents of the table
cur.execute('SELECT * from Capitals')
print(cur.fetchall())

# Retrieve the populations of the provinces and capitals
# (in a list of tuples of the form [province population, capital population])
cur.execute('''
            SELECT P.Population, C.Population
            FROM Density P INNER JOIN Capitals C
            WHERE (P.Name == C.Name)
            ''')
print(cur.fetchall())

# Retrieve the land area of the provinces whose capitals have populations greater than 100,000
cur.execute('SELECT Area from Density WHERE Name IN (SELECT Name from Capitals WHERE Population > 100000)')
print(cur.fetchall())

# Retrieve the provinces with land densities less than two people per square kilometer and 
# capital city populations more than 500,000
cur.execute('SELECT Name from Density WHERE (Population / Area < 2) AND Name IN (SELECT Name from Capitals WHERE Population > 500000)')
print(cur.fetchall())

# Retrieve the total land area of Canada
cur.execute('SELECT sum(Area) from Density')
print(cur.fetchall())

# Retrieve the average capital city population
cur.execute('SELECT avg(Population) from Capitals')
print(cur.fetchall())

# Retrieve the lowest capital city population
cur.execute('SELECT min(Population) from Capitals')
print(cur.fetchall())

# Retrieve the highest province/territory population
cur.execute('SELECT max(Population) from Density')
print(cur.fetchall())

# Retrieve the provinces that have land densities within 0.5 persons per
# square kilometer of one another — have each pair of provinces reported only once
## cur.execute('SELECT (Population / Area), Name AS Density from Density ASC')
## for item in cur.fetchall():
##    print('%f\t%s' % (item[0], item[1]))

cur.execute('''
            SELECT A.Name, B.Name, (A.Population / A.Area) AS ADensity, (B.Population / B.Area) AS BDensity
            FROM Density A INNER JOIN Density B
            WHERE (
                ((A.Population / A.Area) - (B.Population / B.Area)) < 0.5
                )
            AND (
                ((A.Population / A.Area) - (B.Population / B.Area)) >= 0.0
                )
            AND (A.Name != B.Name)
            ''')
print(cur.fetchall())