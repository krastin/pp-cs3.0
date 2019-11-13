import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Numbers')

cur.execute('CREATE TABLE Numbers(Val INTEGER)')
cur.execute('INSERT INTO Numbers Values(1)')
cur.execute('INSERT INTO Numbers Values(2)')

con.commit()

cur.execute('SELECT * FROM Numbers')
print(cur.fetchall())

cur.execute('SELECT * FROM Numbers WHERE 1/0')
print(cur.fetchall())

cur.execute('SELECT * FROM Numbers WHERE 1/0 AND Val > 0')
print(cur.fetchall())

cur.execute('SELECT * FROM Numbers WHERE Val > 0 AND 1/0')
print(cur.fetchall())

# Apparently division by zero is special in SQL and does not equal TRUE
# Hence queries fail the WHERE clause

con.close()