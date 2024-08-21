from pessoa import Pessoa

p1 = Pessoa('Matheus',25)
p2 = Pessoa('Paizante',26)
p1.comer('Maçã')
p2.comer("Pizza")
p1.comer("Bacon")
p1.parar_comer()
p1.comer("Bala")
p1.falar()


#print(f'Nome: {p1.nome}, Idade: {p1.idade}, Está comendo: {"Sim" if p1.comendo else "Não"}, Está falando: {"Sim" if p1.falando else "Não"}')