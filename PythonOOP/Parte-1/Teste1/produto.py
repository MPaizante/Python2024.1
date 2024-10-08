class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = float(preco)

    def desconto(self,percentual):
        self.preco = self.preco - (self.preco*(float(percentual)/100))
        return self.preco

    #Getter
    @property
    def preco(self):
        return self._preco
    #Setter
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace("R$",''))
            return
        self._preco = valor
        return
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,valor):
        self._nome = valor.title()
        return 


p1 = Produto('CAMISETA',50)
p1.desconto(10)
print(p1.nome,p1.preco)

p2 = Produto('caneca',15)
p2.desconto(10)
print(p2.nome,p2.preco)