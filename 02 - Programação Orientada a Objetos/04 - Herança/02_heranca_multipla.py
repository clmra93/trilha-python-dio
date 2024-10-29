class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(cor_pelo, **kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(cor_bico, **kw)

class Cachorro(Mamifero):
    def __init__(self, raca, **kw):
        self.raca = raca
        super().__init__(raca, **kw)

class Gato(Mamifero):
    def __init__(self, brinquedo_favorito, **kw):
        self.brinquedo_favorito = brinquedo_favorito
        super().__init__(brinquedo_favorito, **kw)

class Leao(Mamifero):
    def __init__(self, habitat, **kw):
        self.habitat = habitat
        super().__init__(habitat, **kw)

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, **kw):
        super().__init__(**kw)


gato = Gato("bolinha", nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)

cachorro = Cachorro("poodle", "Preto e branco", 4)
print(cachorro)

leao = Leao("Amazônia", "Amarelo", 4)
print(leao)

