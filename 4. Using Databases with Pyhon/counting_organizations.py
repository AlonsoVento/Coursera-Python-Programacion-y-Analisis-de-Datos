import sqlite3

conn = sqlite3.connect('counting_organizations.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Specify the full path to mbox.txt
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'b:/OneDrive/UPC - Grabaciones de Clases/Python - Programación y Análisis de Datos/SCRIPTS - Coursera - Python - Programación y Análisis de Datos/4. Using Databases with Pyhon/mbox.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1].split('@')[-1]  # Extract domain from org address
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print('Top 10 organizations:')
for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()