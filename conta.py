
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Criando objeto na memória...{}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('O titular {} tem um saldo de {}'.format(self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor