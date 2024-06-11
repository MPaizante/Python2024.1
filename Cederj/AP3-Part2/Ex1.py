i = int(input('Entrada 1 :'))
j = int(input('Entrada 2 :'))
k = int(input('Entrada 3 :'))
lista = []
for l in range(i):
    if len(lista) == i:
        break
    lista.append(j)
    j+=k
    if len(lista) == i:
        break
    lista.append(k)
    k+=j
    if len(lista) == i:
        break
print(lista)
def par(x,elemento):
    pares = []
    for i in x:
        if i %2 ==0:
            pares.append(i)
    if len(pares) == 0:
        return f'Não há elementos pares na sequência até a posição {elemento}'
    return pares
print(par(lista,i))

def quadrado(x):
    q = []
    for i in x:
        for j in range(2,i):
            if i / j == j:
                q.append(i)
    if len(q) == 0:
        return f'Não há elemento par quadrado perfeito.'
    else:
        return q
print(quadrado(lista))