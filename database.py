import sqlite3
from datetime import datetime, timedelta
from config import SUBSCRIPTION_DAYS

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    subscribe_date TEXT,
    expire_date TEXT
)
''')
conn.commit()

def add_user(user_id: int):
    now = datetime.utcnow()
    expire = now + timedelta(days=SUBSCRIPTION_DAYS)
    cursor.execute("REPLACE INTO users (user_id, subscribe_date, expire_date) VALUES (?, ?, ?)",
                   (user_id, now.isoformat(), expire.isoformat()))
    conn.commit()

def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_user_expiry(user_id):
    cursor.execute("SELECT expire_date FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if row:
        return datetime.fromisoformat(row[0])
    return None

def remove_user(user_id):
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()