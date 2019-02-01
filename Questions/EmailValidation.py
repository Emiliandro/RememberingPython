import re

class EmailValidation:
    def __init__(self,valor):
        self.__resposta = self.calculo(valor)

    @property
    def resposta(self):
        return self.__resposta

    def calculo(self,valor):
        if re.match(r"[a-z0-9]+@[a-z0-9]+.[a-z0-9]+",valor):
            return True
        else:
            return False

if __name__ == "__main__":

    print EmailValidation('email#falso.com').resposta
    print EmailValidation('email@verdadeiro.com').resposta