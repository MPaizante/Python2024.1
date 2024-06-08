entrada = input('Entrada:  ').split()
entrada = [int(n) for n in entrada]
import random
matriz = []
for i in range(entrada[0]):
    lista = []
    for j in range(entrada[1]):
        lista.append(random.randint(10,99))
    matriz.append(lista)

print('Matriz:')
for i in matriz:
    linha = [str(n) for n in i]
    frase = ''
    for j in linha:
        frase += j + ' '
    print(frase)
print('Conteúdo da linha com maior valor:')
soma = 0
maior = 0
linha = []
a = ''
for i in matriz:
    for j in i:
        soma += j
    if soma >= maior:
        maior = soma
        linha = i
linha = [str(n) for n in linha]
for i in linha:
    a += i + ' '
print(a)

coluna = []
soma = 0
maior = 0
c = ''
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma += j

