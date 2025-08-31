import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input('Informe o id do cliente: ')
cursor.execute(f'SELECT * FROM clientes WHERE id={id_cliente}')
cliente = cursor.fetchone()
print(dict(cliente))

# # Evite isso
# id = 1
# cursor.execute('SELECT * FROM minha_tabela WHERE id = ' + str(id))

# # Faça isto:
# id = 1
# cursor.execute('SELECT * FROM minha_tabela WHERE id = ?', (id,))

