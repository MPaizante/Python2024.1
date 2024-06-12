entrada =input('Digite:====  ')
with open(entrada,'r') as arquivo:
    d = dict()
    for i in arquivo:
        linha = i.split()
        for u in linha:
            if u in d:
                d[u] += 1
            else:
                d[u] = 1
matriz = list(d)

def ordem(lista):
    for i in range(len(lista)):
        for j in range(1, len(lista) - i):
            if lista[j-1] > lista[j]:
                lista[j-1],lista[j] = lista[j],lista[j-1]
    return lista
ordenado = ordem(matriz)
print(ordenado)
for i in ordenado:
    if d[i] > 1:
        print(f'{i} ocooreu {d[i]} vezes')
    else:
        print(f'{i} ocooreu {d[i]} vez')