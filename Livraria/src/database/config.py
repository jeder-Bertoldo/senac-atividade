import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # substitua pelo seu usuário do MySQL
        password="",  # substitua pela sua senha do MySQL
        database="gerenciador_livros"
    )
    return conn
