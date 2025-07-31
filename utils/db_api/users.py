import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE telegram_id=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def add_user(telegram_id, full_name, phone):
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (telegram_id, full_name, phone) VALUES (?, ?, ?)",
                   (telegram_id, full_name, phone))
    conn.commit()
    conn.close()
