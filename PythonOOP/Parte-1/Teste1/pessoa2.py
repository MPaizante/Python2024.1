import random
class Pessoa:
    ano_autal = 2024
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def nascimento(self):
        print(self.ano_autal - self.idade)

    @classmethod
    def ano_nascimento(cls,nome, ano):
        idade = cls.ano_autal - ano
        return  cls(nome,idade)

    @staticmethod
    def gera_id():
        rand =random.randint(100,900)
        return rand

p1 = Pessoa.ano_nascimento('Luiz', 1987)
p2 = Pessoa('Carlos',32)
print(p1.nome,',',p1.idade)
p2.nascimento()
print(p1.gera_id())