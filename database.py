import sqlite3

conn = sqlite3.connect(database="claims.db")

cursor = conn.cursor()

cursor.execute("""
Create table if not exists claims (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim TEXT NOT NULL,
    verdict TEXT NOT NULL,
    reasoning TEXT NOT NULL,
    confidence REAL NOT NULL,
    status TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            
)
""")

conn.commit()

conn.close()