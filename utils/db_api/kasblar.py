import sqlite3

def get_all_kasblar():
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM kasblar")
    result = [row[0] for row in cursor.fetchall()]
    conn.close()
    return result

def add_kasb(name: str) -> bool:
    try:
        conn = sqlite3.connect("data/database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO kasblar (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        return True
    except:
        return False
    
def delete_kasb(name: str) -> bool:
    try:
        conn = sqlite3.connect("data/database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM kasblar WHERE name = ?", (name,))
        conn.commit()
        conn.close()
        return True
    except:
        return False