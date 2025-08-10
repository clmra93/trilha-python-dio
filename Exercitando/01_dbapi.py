import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / 'meu_db.sqlite')
cursor = conn.cursor()

def criar_tabela(cursor):
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VAVHAR(100), email VARCHAR(150))'
    )
    conn.commit()

def inserir_registro(conn, cursor, nome, email):
    data = (nome, email)
    cursor.execute(f'INSERT INTO clientes (nome, email) VALUES (?,?);', (data))
    conn.commit()

def atualizar_regitro(conn, cursor, nome, email, id):
    