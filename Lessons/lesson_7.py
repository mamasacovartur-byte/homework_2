import sqlite3

def create_table(connection):
    connection.execute("DROP TABLE IF EXISTS students")
    connection.execute("""
    CREATE TABLE students(
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)
    connection.commit()

def add_students(name, age, city):
    conn.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)",
        (name, age, city)
    )
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_table(conn)
    add_students('Artur', 17, 'Bishkek')
import sqlite3

def create_table(connection):
    connection.execute("DROP TABLE IF EXISTS students")
    connection.execute("""
    CREATE TABLE students(
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)
    connection.commit()

def add_students(connection, name, age, city):
    connection.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)",
        (name, age, city)
    )
    connection.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_table(conn)
    add_students(conn, 'Artur', 17, 'Bishkek')

    conn.close()
