contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError
# aqui como a chave não existe, dá erro, lança uma exceção

resultado = contatos.get("chave")  # None
print(resultado)
# aqui você consegue saber se tem a chave ou não no dicionário

resultado = contatos.get("chave", {})  # {}
print(resultado)
# aqui você define que se nao encontrar a chave retorna o valor passado no argumento, nesse caso, dicionário vazio

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
# aqui é outro exemplo de como consultar se a chave é existente