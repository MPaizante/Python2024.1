class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    def inserir_produto(self,produtos):
        self.produtos.append(produtos)
    def lista_produto(self):
        for p in self.produtos:
            print(p.nome,p.valor)
    def soma_total(self):
        total = 0
        for p in self.produtos:
            total += p.valor
        return total

class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor
class Cliente:
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade
        self._enderecos = []
    def insere_endereco(self,cidade,estado):
        self._enderecos.append(Endereco(cidade,estado))
    def lista_endereco(self):
        for e in self._enderecos:
            print(e._cidade,e._estado)
    def __del__(self):
        print(f'{self._nome} foi apagado!')

class Endereco:
    def __init__(self,cidade,estado):
        self._cidade = cidade
        self._estado = estado
    def __del__(self):
        print(f'{self._cidade} - {self._estado} foi apagado')
