from database.generate import create_connection


def insert_data(name, price, store, date):
    cursor, conn = create_connection()
    cursor.execute('''INSERT INTO products (name, price, store, date) 
                   VALUES (?, ?, ?, ?)''', (name, price, store, date))
    conn.commit()
