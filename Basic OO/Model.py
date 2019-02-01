class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.duracao = duracao



class Seriado(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.capitalize()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme('vingadores','2018','3 horas')
demolidor = Seriado('demolidor','2014','3 temporadas')

filmes_e_series = [vingadores, demolidor]

for programa in filmes_e_series:
    print('O programa ou filme ' + programa.nome + ' eh de ' + programa.ano)
