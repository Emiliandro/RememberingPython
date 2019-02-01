
class Orcamento(object):
    def __init__(self,valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto(orcamento)
        print imposto_calculado
