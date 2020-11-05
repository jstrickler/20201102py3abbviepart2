import sqlite3

data_file = 'EXAMPLES/django2/contacts/contacts.db'

with sqlite3.connect(data_file) as conn:

    cur = conn.cursor()

    cur.execute('select * from contacts')

    for row in cur.fetchall():
        print(row)
