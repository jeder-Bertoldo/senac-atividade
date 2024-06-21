from database.config import get_db_connection
from utils.book import Book
import mysql.connector

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            titulo VARCHAR(100) NOT NULL,
            autor VARCHAR(100) NOT NULL,
            sinopse TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_book(nome, titulo, autor, sinopse):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (nome, titulo, autor, sinopse) VALUES (%s, %s, %s, %s)', (nome, titulo, autor, sinopse))
    conn.commit()
    conn.close()

def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    rows = cursor.fetchall()
    books = [Book(row[0], row[1], row[2], row[3], row[4]) for row in rows]
    conn.close()
    return books

def update_book(id, nome, titulo, autor, sinopse):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE livros SET nome = %s, titulo = %s, autor = %s, sinopse = %s WHERE id = %s', (nome, titulo, autor, sinopse, id))
        conn.commit()
        print("Livro atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conn.close()

def delete_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = %s', (id,))
    conn.commit()
    conn.close()
