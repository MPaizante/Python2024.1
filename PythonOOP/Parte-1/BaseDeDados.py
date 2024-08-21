class BaseDeDados(object):
    def __init__(self):
        self.__dados = {}
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id,name in self.__dados['clientes'].items():
            print(id,name)
    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]




bd = BaseDeDados()
bd.inserir_cliente(1,'Matheus')
bd.inserir_cliente(2,'Paizante')
bd.inserir_cliente(3,'Araujo')
print(bd.dados)
bd.lista_clientes()
