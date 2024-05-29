i = int(input("Digite: "))
j = int(input("Digite: "))
k = int(input("Digite: "))
def sequencia(a,b,c):
    lista = []
    for n in range(a):
        lista.append(b)
        b += c
        if len(lista) == i:
            break
        lista.append(c)
        c += b
        if len(lista) == i:
            break
    return lista
lista = sequencia(i,j,k)
print(lista)
print(f'Os {i} elementos da sequência são {lista}')
def pares(x,a):
    lista = []
    for i in x:
        if i % 2 == 0:
            lista.append(i)
    if len(lista) == 0:
        return f'Não há elementos pares na sequência até a posição {a}'
    return lista
par = pares(lista,i)
print(f'Os elementos pares da sequência são {par}')

def quadrado(x):
    q = []
    for i in x:
        for u in range(2,i):
            if i / u == u:
                q.append(i)
    if len(q) == 0:
        return 'Não a quadrado perfeito'
    return f'Dentre esses, os que são quadrado perfeito são {q}'


print(quadrado(lista))




