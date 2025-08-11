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

criar_tabela(cursor)

def inserir_registro(conn, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        f'INSERT INTO clientes (nome, email) VALUES (?,?);', data
    )
    conn.commit()

# inserir_registro(conn, cursor, 'Guilherme', 'gui@gmail.com')

def atualizar_regitro(conn, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute(
        'UPDATE clientes SET nome = ?, email  = ? WHERE id = ?', data
    )
    conn.commit()

# atualizar_regitro(conn, cursor, 'Guilherme', 'gui@gmail.com', 1)

def remover_registro(conn, cursor, id):
    data = (id,)
    cursor.execute(
        'DELETE FROM clientes WHERE id = ?', data
    )
    conn.commit()

# remover_registro(conn, cursor, 1)

def inserir_muitos(conn, cursor, dados):
    cursor.executemany(
        'INSERT INTO clientes (nome, email) VALUES (?, ?)', dados
    )
    conn.commit()

# dados = [
#     ('Guilherme', 'gui@gmail.com'),
#     ('Chapie', 'chapie@gmail.com'),
#     ('Melanie', 'melanie@gmail.com'),
#     ('Thompson', 'thompson@gmail.com'),
#     ('Carllie', 'carllie@gmail.com'),
# ]
# inserir_muitos(conn, cursor, dados)

def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    return cursor.fetchone()

# cliente = recuperar_cliente(cursor, 2)
# print(cliente)

# fetchone() pode ser usado para recuperar um único registro de resultado. Ele retorna o próximo registro na lista de resultados ou 'None' se não houver mais resultados.

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes;')

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)

# o fetchall() pode ser usado para recuperar todos os registros de resultados de uma vez. Ele retorna uma lista de registros ou uma lista vazia se não houver mais resultados.

def listar_clientes_ordem_alfabetica_crescente(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome ASC;')

clientes = listar_clientes_ordem_alfabetica_crescente(cursor)
for cliente in clientes:
    print(cliente)

def listar_clientes_ordem_alfabetica_decrescente(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome DESC;')

clientes = listar_clientes_ordem_alfabetica_decrescente(cursor)
for cliente in clientes:
    print(cliente)
