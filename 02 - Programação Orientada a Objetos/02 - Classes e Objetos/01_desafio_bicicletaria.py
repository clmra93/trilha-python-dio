class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def get_cor(self):
        return self.cor # Esse método retorna o atributo que é chamado, neste caso, cor.
    # Não é uma forma muito usada em Python

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    # Aqui conseguimos exibir nossa instância


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
Bicicleta.buzinar(b2) # É o mesmo que b2.buzinar()
print(b2.get_cor())

class Carro:
    def __init__(self, cor, ano, modelo, km, valor):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.km = km
        self.valor = valor

    def andar(self):
        print("Carro andando")

    def parando(self):
        print("Carro parando!")

c1 = Carro("preto", 2008, "corsa", 200000, 23000)
c1.andar()
c1.parando()
print(c1.cor, c1.ano, c1.modelo, c1.km, c1.valor)

class Frutas:
    def __init__(self, cor, sabor, nome):
        self.cor = cor
        self.sabor = sabor
        self.nome = nome

f1 = Frutas("vermelha", "doce", "melância")
print(f1.cor, f1.sabor, f1.nome)

f2 = Frutas("verde", "azedo", "kiwi")
print(f2.cor, f2.sabor, f2.nome)

f3 = Frutas("amarela", "doce", "melão")
print(f3.cor, f3.sabor, f3.nome)