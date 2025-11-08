# db_app.py (After Fix)
import sqlite3

def get_user_data(username: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # ✅ Secure parameterized query
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()
