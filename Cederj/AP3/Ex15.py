entrada = input('Entrada? ')
matriz = []
with open(entrada,'r') as arquivo:
    for i in arquivo:
        linha = i.split()
        linha = [int(n) for n in linha]
        matriz.append(linha)
