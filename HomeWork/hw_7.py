import sqlite3

def create_table(connection):
    connection.execute("DROP TABLE IF EXISTS books")
    connection.execute("""
    CREATE TABLE books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    connection.commit()

def add_books(connection, id, name, author, publication_year, genre, number_of_pages, number_of_copies):
    connection.execute(
        "INSERT INTO books (id, name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (id, name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    connection.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_table(conn)
    add_books(conn, 1, 'Белый пароход', 'Ч.Т. Айтматов', 1991, 'мелодрама', 183, 12390)

    conn.close()