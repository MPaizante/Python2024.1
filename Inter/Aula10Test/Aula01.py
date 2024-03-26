def linha():
    lista = []
    while True:
        linha = input('Digite: ')
        if not linha:
            break
        lista.append(linha)
        lista = [float(num) for num in lista]
    return lista
def maior(lista):
    maior = lista[-1]
    lista_maior = []
    for i in lista:
        if i > maior:
            lista_maior.append(i)
    return lista_maior


numeros = linha()
maiores = maior(numeros)
print(f'Relação dos numeros maiores que {numeros[-1]}: ')
for i in maiores:
    print(i)