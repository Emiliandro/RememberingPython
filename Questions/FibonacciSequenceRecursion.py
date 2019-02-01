class FibonacciSequenceRecursion:
    def __init__(self, valor):
        self.inputDaQuestao = valor

    def calculo(self, valor):
        a, b = 0, 1
        for i in xrange(0, valor):
            yield "{}:: {}".format(i + 1, a)
            a, b = b, a + b

    def respostaDaQuestao(self):
        for item in self.calculo(self.inputDaQuestao):
            print item

if __name__ == "__main__":

    quociente = FibonacciSequenceRecursion(16)
    quociente.respostaDaQuestao()