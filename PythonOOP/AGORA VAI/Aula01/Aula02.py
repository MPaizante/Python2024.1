from symtable import Class


class NPC:
    def __init__(self, nome , time , forca , municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Time: {self.time}")
        print(f"Força:{self.forca}")
        print(f"Munição: {self.municao}")
        print(f"Vivo: {"sim" if self.vivo else "não"}")
        print(f"Energia: {self.energia}")
        print('-'*40)

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()
class Guarda(NPC):
    def __init__(self, nome , time):
        self.forca = 100
        self.municao = 200
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()
class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()
s1 = Guarda("Olho Vivo", 1)
s2 = Soldado("Banha nha agunha", 1)
s3 = Elite("Ninja", 1)
s4 = Guarda("Super", 2)
s5 = Soldado("COWBOY", 2)
s6 = Elite("Fortão", 2)

s1.info()