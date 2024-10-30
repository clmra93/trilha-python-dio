class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # Decorador property presseguido de @. É uma função que executa antes da sua funcção. 
    def x(self): # Só com isso você já tem o atributo x disponível na sua classe, pode deferir o processo de atribuição e dereção.
        return self._x or 0 # O property pega o método e transforma em propriedade.

    @x.setter # Aqui o setter faz a modificação, ele permite setar o x.
    def x(self, value): # O setter permite a atribuição de valor, a alteração da propriedade
        self._x += value

    @x.deleter # Aqui o deleter permite deletar o x.
    def x(self):
        self._x = 0 # Se quiser atribuir o (-1) por exemplo é só colocar o -1 no lugar do 0. O 0 vai excluir o valor e atribuir o 0 ao valor


foo = Foo(10) # Aqui instância com o objeto tipo foo
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
