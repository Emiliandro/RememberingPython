class BasicMath:
    def __init__(self,valor1,valor2):
        self.__adicao = valor1+valor2
        self.__subtracao = valor1-valor2
        self.__multiplicacao = valor1*valor2
        self.__divisao = valor1/valor2
        self.__resto = valor1%valor2
        self.__quociente = valor1//valor2
        self.__potenciacao = valor1**valor2

    @property
    def adicao(self):
        return self.__adicao
    @property
    def subtracao(self):
        return self.__subtracao
    @property
    def multiplicacao(self):
        return self.__multiplicacao
    @property
    def divisao(self):
        return self.__divisao
    @property
    def resto(self):
        return self.__resto
    @property
    def quociente(self):
        return self.__quociente
    @property
    def potenciacao(self):
        return self.__potenciacao

if __name__ == "__main__":

    print BasicMath(5,5).adicao
    print BasicMath(5,5).subtracao
    print BasicMath(5,5).multiplicacao
    print BasicMath(5,5).divisao
    print BasicMath(5,5).resto
    print BasicMath(5,5).quociente
    print BasicMath(5,5).potenciacao