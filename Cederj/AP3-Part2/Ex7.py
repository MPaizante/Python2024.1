i = int(input('Entrada i:'))
j = int(input('Entrada j:'))
k = int(input('Entrada k:'))
lista = []
while True:
    if len(lista) == i:
        break
    else:
        lista.append(j)
        j += k
    if len(lista) == i:
        break
    else:
        lista.append(k)
        k += j
print(f'Os {i}elementos da sequência são {lista}.')

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
par(lista)

def quadrado(lista):
    q = []
    for i in lista:
        for j in range(2,i):
            if i / j == j:
                q.append(i)
    if len(q) == 0:
        print('Não há elemento par quadrado perfeito.')
        return None
    else:
        print(f'Dentre esses, os que são quadrado perfeito são {q}')
        return None

quadrado(lista)


