import sqlite3

conn = sqlite3.connect("database.db")
db = conn.cursor()

db.execute("""
CREATE TABLE IF NOT EXISTS menu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price REAL,
    image TEXT
)
""")

conn.commit()
conn.close()