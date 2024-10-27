pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)
# Dicionário pessoa. Valores declarados por chave: valor, chave: valor.

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)
# Na classe dict eu passo os parametros. Já declarando chave: valor

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
# Aqui já tem o dicionário criado, e está adicionando uma nova chave nele.

pessoa["nome"] = "Maria"
print(pessoa)
# Aqui troca o nome para Maria