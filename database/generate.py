import sqlite3


def create_database():
    conn = sqlite3.connect('coffee_prices.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price TEXT,
            store TEXT,
            date TEXT
        )
    ''')
    conn.commit()


def create_connection():
    conn = sqlite3.connect('coffee_prices.db')
    cursor = conn.cursor()
    return cursor, conn
