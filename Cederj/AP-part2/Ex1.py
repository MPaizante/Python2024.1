entrada = input('Nome do arquivo: ')
def ler(entrada):
    with open(entrada, 'r') as arquivo:
        for i in arquivo:
            print(i.strip())
    return None
print(f'Conteúdo em {entrada}:')
ler(entrada)
def media(entrada):
    with open(entrada, 'r') as arquivo:
        contador = 0
        valor = 0
        for i in arquivo:
            lista = i.split()
            lista_float = [float(num) for num in lista]
            for u in lista_float:
                valor += u
                contador += 1
        res = valor / contador
    return res
print(f'Média dos Números em {entrada}: {media(entrada)}')
def acima(entrada):
    with open(entrada, 'r') as arquivo:
        valor = media(entrada)
        contador = 0
        for i in arquivo:
            lista = i.split()
            lista_float = [float(num) for num in lista]
            for u in lista_float:
                if u > valor:
                    contador += 1
    return contador
print(f'Quantidade Acima de {media(entrada)} em {entrada}: {acima(entrada)}')

