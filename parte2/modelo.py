class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @property
    def likes(self):
        return self._likes
    
    @property
    def ano(self):
        return self._ano
    

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas


vingadores = Filme('vingadores: guerra infinita','2022','1:30:00')
lost = Serie('lost','2012','13 Temporadas')

for i in range(0,10):
    lost.dar_like()

print(f"Nome: {lost.nome} - Ano: {lost.ano} - Duração: {lost.temporadas} - Curtidas: {lost.likes}")
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Curtidas: {vingadores.likes}")