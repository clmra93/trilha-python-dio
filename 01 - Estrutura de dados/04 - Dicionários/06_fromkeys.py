resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

# O fromkeys cria as chaves no dicionário com valor none
# Se o dicionário for já existente, utiliza o nome do mesmo no lugar de dict