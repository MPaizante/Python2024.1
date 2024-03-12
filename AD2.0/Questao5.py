entrada = input("Entrada: ").split()#entrada dos numeros como str
lista = [int(num) for num in entrada]#loop para transformar em interios
def subprograma(lista):#subprograma para definir elementos repetidos da questao A e sequencia da questao B
    lista2 = []
    repetidos = []
    for list in lista:#loop para questao A
        if list not in lista2:
            lista2.append(list)
        else:
            repetidos.append(list)
    inverso = [lista[i] for i in range(len(lista) - 1, -1, -1)]
    inverso_str = [str(i_str) for i_str in inverso]
    inverso2 =''
    for i in inverso_str:#loop para questao B
        inverso2 += ' ' + i
    return print(f'Os elementos que se repetem são:{repetidos}\n'#saida A
                 f'Sequência inversa: {inverso2}')#saida B

subprograma(lista)#execucao do programa
def subprograma_inversoes(lista):#subprograma questao C
    cont = 0
    inversoes = []
    for i in range(len(lista)):#loop para determinar as inversões e a quantidade de inversões na sequência da entrada.
        for j in range( i +1, len(lista)):
            if lista[i] > lista[j]:
                cont += 1
                inversoes.append((i,j))

    return print(f'Há {cont} inversões, e as posições são: {inversoes}')#Saida C
subprograma_inversoes(lista)#Execucao C


