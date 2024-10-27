# O set retira os elementos duplicados

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}
# Neste exemplo ele retira as letras que se repetem dentro da palavra

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"} # {"gol", "palio", "celta"}

# O set não garante a ordem. Cada vez que executar, vai ser apresentado uma ordem diferente.

linguagens = set(("python", "java", "python"))
print(linguagens)
# {'java', 'python'}

linguagens = {"python", "java", "python"}
print(linguagens)
# {'python', 'java'}