def mostra(lista):
    print(f'Os {len(lista)} elementos da sequência são {lista}')
    return None


def par(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    if len(pares) == 0:
        print(f'Não há elementos pares na sequência até a posição {len(lista)}')
        return None
    else:
        print(f'Os elementos pares da sequência são {pares}.')
        return None


def quadrado(lista):
    q = []
    primo = []
    for i in lista:
        p = False
        for j in range(2, i):
            if i / j == j:
                q.append(i)
        for u in range(2, i):
            if i / u == 0:
                p = True
        if p == False:
            primo.append(i)

    if len(q) > 0 and len(primo) > 0:
        print(f'Dentre esses, os que são quadrado perfeito são {q}')
        print(f'Dentre esses, os que são primos são {primo}')
        return None
    elif len(q) > 0:
        print(f'Dentre esses, os que são quadrado perfeito são {q}')
        return None
    elif len(primo) > 0:
        print(f'Dentre esses, os que são primos são {primo}')
        return None
    else:
        print('Não há elemento quadrado perfeito.')
        print('Não há elemento primos.')
        return None



i = int(input('Digite i:'))
k = int(input('Digite k:'))
j = int(input('Digite j:'))
matriz = []

while True:
    if len(matriz) == i:
        break
    else:
        matriz.append(k)
        k+= j
    if len(matriz) == i:
        break
    else:
        matriz.append(j)
        j += k

mostra(matriz)
par(matriz)
quadrado(matriz)
