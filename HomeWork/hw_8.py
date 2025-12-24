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

def add_books(connection, name, author, publication_year, genre, number_of_pages, number_of_copies):
    connection.execute(
        "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?)",
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    connection.commit()

def delete_books(connection, book_id):
    connection.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )
    connection.commit()

def update_book_name(connection, book_id, new_name):
    connection.execute(
        "UPDATE books SET name = ? WHERE id = ?",
        (new_name, book_id)
    )
    connection.commit()

def get_all_books(connection):
    result = connection.execute(
        "SELECT * FROM books"
    )
    return result.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    create_table(conn)

    add_books(conn, 'Белый пароход', 'Ч.Т. Айтматов', 1991, 'мелодрама', 183, 5)
    add_books(conn, 'Материнское поле', 'Ч.Т. Айтматов', 1963, 'драма', 210, 3)

    print(get_all_books(conn))

    update_book_name(conn, 1, 'Белый пароход (обновлено)')
    print(get_all_books(conn))

    delete_books(conn, 2)
    print(get_all_books(conn))

    conn.close()
