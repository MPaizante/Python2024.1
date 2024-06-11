entrada = input('Entrada:  ')
valor = input('Numero: ').split()
valor = [int(n) for n in valor]
seis = 0
cinco = 0
quatro = 0
tres = 0
with open(entrada,'r') as arquivo:
    for i in arquivo:
        print(i.strip())

with open(entrada,'r') as arquivo:
    for i in arquivo:
        linha = i.split()
        linha = [int(n) for n in linha]
        