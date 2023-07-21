class Cliente:

    def __init__(self,nome):
        self.__nome = nome.capitalize()

    @property
    def nome(self):
        return self.__nome.upper()
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome