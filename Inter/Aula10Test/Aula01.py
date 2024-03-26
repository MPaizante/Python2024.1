def lista(x):
    lista = []
    for i in range(x):
        numeros = int(input('Numero: '))
        lista.append(numeros)
    return lista
def menor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor
def maior(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior
def media(lista):
    c = 0
    for i in lista:
        c += i
    return c
entrada = int(input('Quantos numeros quer ler?: '))
valor = lista(entrada)
print(f'Menor dos {entrada} numeros lidos foi: {menor(valor)}')
print(f'Maior dos {entrada} numeros lidos foi: {maior(valor)}')
print(f'A media dos {entrada} numeros foi {(media(valor)/len(valor)):,.2f}')