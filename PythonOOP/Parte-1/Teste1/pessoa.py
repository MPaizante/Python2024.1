class Pessoa:
    def __init__(self,nome,idade,comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando  = falando

    def falar(self):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo!')
        else:
            if self.falando:
                print(f'{self.nome} já está falando!')
            else:
                self.falando = True
                print("AAAAAAAAAAAAAAAAAAAAAAAAAA!")
        return
    def parar_falar(self):
        if self.falando:
            print(f"{self.nome} parou de falar!")
            self.falando = False
        else:
            print(f"{self.nome} já estava quieto!")
        return

    def comer(self,alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
        else:
            self.comendo = True
            print(f'{self.nome} está comendo {alimento}.')
        return

    def parar_comer(self):
        if self.comendo:
            self.comendo = False
            print(f'{self.nome} parou de comer! ')
        else:
            print(f'{self.nome} não estava comendo!')
