class Escritor(object):
    def __init__(self,nome):
        self.__nome = nome
        self.__ferramenta = None
    @property
    def ferramenta(self):
        return self.__ferramenta
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta
    @property
    def nome(self):
        return self.__nome


class Caneta(object):
    def __init__(self,marca):
        self.__marca = marca
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta escrevendo...')

class MaquinaDeEscrever:
    def __init__(self,marca):
        self.__marca = marca
    @property
    def marca(self):
        return self.__marca
    def escrever(self):
        print('Maquina escrevendo...')