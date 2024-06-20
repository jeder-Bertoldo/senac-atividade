from src.database.config import get_db_connection
from src.models.livro import Livro

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS
    livros (
                   id INT AUTO_INCREMENT
    PRIMARY KEY,
                   nome VARCHAR(100) NOT NULL,
                   titulo VARCHAR(100)NOT NULL,
                    autor VARCHAR(100) NOT NULL,
                   sinopse TEXT
    )
''')

    conn.commit()
    conn.close()

def add_livro(nome, titulo, autor, sinopse):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (nome, titulo, autor, sinopse) VALUES (%s, %s, %s, %s)' (nome, titulo, autor, sinopse))
    conn.commit()
    conn.close()

def get_livro():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    rows = cursor.fetchall()
    Livros = [Livro(row[0], row[1], row[2], row[3], row[4]) for row in rows ]
    conn.close()
    return Livros

def update_livro():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE livros SET nome = %s, titulo = %s, autor = %s, sinopse = %s WHERE = id %s', (nome, titulo, autor, sinopse, id))
    conn.commit()
    conn.close()

def delete_livro(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = %s', (id,))
    conn.commit()
    conn.close()