import mysql.connector

def get_db_connection():
    conn = mysql.connector(
        host = "localhost",
        user = "root",
        password = "",
        database = "nome_banco"
    )
    return conn