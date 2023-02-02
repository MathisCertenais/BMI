import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, height_value, weight_value) VALUES (?, ?, ?, ?)",
            ('Alice', '21.24', '80', '185')
            )

cur.execute("INSERT INTO posts (title, content, height_value, weight_value) VALUES (?, ?, ?, ?)",
            ('Bob', '32.89', '80', '185')
            )

connection.commit()
connection.close()