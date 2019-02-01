# TEMPLATE METHODS

from abc import ABCMeta, abstractmethod

class TemplateCondicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deveUsarMaximaTaxacao(orcamento):
            return self.MaximaTaxacao(orcamento)
        else:
            return self.MinimaTaxacao(orcamento)

    @abstractmethod
    def deveUsarMaximaTaxacao(self, orcamento):
        pass

    @abstractmethod
    def MaximaTaxacao(self, orcamento):
        pass

    @abstractmethod
    def MinimaTaxacao(self, orcamento):
        pass

# METODOS DOS IMPOSTOS

def calcula_ISS(orcamento):
    return orcamento.valor * 0.1


def calcula_ICMS(orcamento):
    return orcamento.valor * 0.06

def cacula_ICPP(orcamento):
    return ICPP().calcula(orcamento)

# TEMPLATES APLICADOS

class ICPP(TemplateCondicional):
    def deveUsarMaximaTaxacao(self, orcamento):
        return orcamento.valor > 500

    def MaximaTaxacao(self, orcamento):
        return orcamento.valor * 0.07

    def MinimaTaxacao(self, orcamento):
        return orcamento.valor * 0.05