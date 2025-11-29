import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price TEXT,
    link TEXT,
    image_link TEXT,
    price_num REAL
)
""")

conn.commit()
conn.close()

print("Fresh database created successfully!")
