import sqlite3

def init_db():
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_info (
            id INTEGER PRIMARY KEY,
            mobile TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(mobile, email):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_info (mobile, email) VALUES (?, ?)', (mobile, email))
    conn.commit()
    conn.close()
