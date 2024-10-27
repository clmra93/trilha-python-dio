contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])
# Quando está iterando dicionário, passa linha a linha do dicionário, retornando a chave, no caso, a primeira string
# Para acessar tudo, preciso colocar o nome do dicionário, nesse caso contatos, e a chave que quer acessar entre colchetes

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)
# Aqui temos outra forma de obter o mesmo resultado