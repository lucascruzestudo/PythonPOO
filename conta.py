class Conta: 

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f"Construiu o objeto {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    

