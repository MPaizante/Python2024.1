entrada = input("Entrada: ").split()
lista = [int(num) for num in entrada]
def subprograma(lista):
    lista2 = []
    repetidos = []
    for list in lista:
        if list not in lista2:
            lista2.append(list)
        else:
            repetidos.append(list)
    inverso = [lista[i] for i in range(len(lista) - 1, -1, -1)]
    inverso_str = [str(i_str) for i_str in inverso]
    inverso2 =''
    for i in inverso_str:
        inverso2 += ' ' + i
    return print(f'Os elementos que se repetem são:{repetidos}\n'
                 f'Sequência inversa: {inverso2}')

subprograma(lista)
def subprograma_inversoes(lista):
    cont = 0
    inversoes = []
    for i in range(len(lista)):
        for j in range( i +1, len(lista)):
            if lista[i] > lista[j]:
                cont += 1
                inversoes.append((i,j))

    return print(f'Há {cont} inversões, e as posições são: {inversoes}')
subprograma_inversoes(lista)


