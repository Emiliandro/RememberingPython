import math

class PrimeChecker:
    def __init__(self,valor):
        self.resposta = self.calculo(valor)

    def calculo(self,valor):
        if valor % 2 == 0 and valor > 2:
            return False
        else:
            return all(valor % i for i in range(3,int(math.sqrt(valor)) + 1,2))

if __name__ == "__main__":

    print PrimeChecker(37).resposta
    print PrimeChecker(100).resposta
    print PrimeChecker(77).resposta
    print PrimeChecker(88).resposta
    print PrimeChecker(2).resposta