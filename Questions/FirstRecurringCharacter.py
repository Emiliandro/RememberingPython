# FirstRecurringCharacter
# DBCABA = B

class FirstRecurringCharacter:
    def resultado(self, questao):
        self.resposta = self.contagem(questao)
        print self.resposta

    def contagem(self, questao):
        __counts = {}
        for char in questao:
            if char in __counts:
                return char
            else:
                __counts[char] = 1

        return None

if __name__ == "__main__":

    FirstRecurringCharacter().resultado('KJHGFK')
    FirstRecurringCharacter().resultado('KJHGFF')
    FirstRecurringCharacter().resultado('KJHGFO')
