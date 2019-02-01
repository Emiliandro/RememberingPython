class Page():
    def __init__(self, h1, titulo):
        self.__h1 = h1
        self.__title = titulo
        self.__head = '<html lang="en"><head><title>' + self.__title + '</title><meta charset="UTF-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /></head>'
        self.__body = '<body>' + self.__h1 + '</body>'
        self.__footer = '<footer>' + '</footer></html>'

    @property
    def h1(self):
        return self.__h1

    def set_h1(self, valor):
         self.__h1 = '<h1>' + valor + '</h1>'
         self.chamadas_de_alteracao()
         return print('h1 alterado')

    @property
    def title(self):
        return self.__h1

    def set_title(self, valor):
         self.__title = valor
         self.chamadas_de_alteracao()
         return print('title alterado')

    def chamadas_de_alteracao(self):
        self.__head = '<html lang="en"><head><title>' + self.__title + '</title><meta charset="UTF-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /></head>'
        self.__body = '<body>' + self.__h1 + '</body>'
        self.__footer = '<footer>' + '</footer></html>'


    @property
    def imprimi(self):
        return '' + self.__head + self.__body + self.__footer + ''
