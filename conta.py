class Conta: 

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f"Construiu o objeto {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__titular}: R$ {self.__saldo}")
    
    def depositar(self, valor):
        self.__saldo += valor

    def __verificar_saque(self,valor_saque):
        valor_disponivel = self.saldo + self.limite
        return valor_saque <= valor_disponivel

    def sacar(self, valor):
        if self.__verificar_saque(valor):
            self.__saldo -= valor
        else:
            print(f"Saque R$ {valor} maior do que o saldo e limite combinados.")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    
    

