entrada = input('Digite: ')
d = dict()
with open(entrada,'r') as arquivo:
    for i in arquivo:
        linha = i.split()
        for j in linha:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
lista = list(d)
def ordena(matriz):
    for i in range(len(matriz)):
        for j in range(i+1,len(matriz)):
            if matriz[j] < matriz[i]:
                matriz[j],matriz[i] = matriz[i],matriz[j]
    return matriz
lista_ordenada = ordena(lista)
for i in lista_ordenada:
    if d[i] > 5:
        print(i)
