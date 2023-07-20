class Conta: 

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f"Construiu o objeto {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo de {self.titular}: R$ {self.saldo}")
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    
    

