import sys

class SumDigits:
    def __init__(self, valor):
        self.resposta = self.calculo(valor)

    def calculo(self,valor):
        linha = valor.rstrip()
        soma = 0
        if linha:
            for item in linha:
                soma += int(item)
            return soma

if __name__ == "__main__":

    print SumDigits('09525267373738000006').resposta