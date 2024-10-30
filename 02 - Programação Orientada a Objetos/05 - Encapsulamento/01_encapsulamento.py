class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor # Forma correta de se acessar atributos privados, visto que é possível implementar uma lógica de validação para acesso aos dados.

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
conta._saldo() # Prática incorreta. Se tem o (_) antes, é um atributo privado, não deve ser acessado diretamente.
print(conta.nro_agencia)
print(conta.mostrar_saldo())
