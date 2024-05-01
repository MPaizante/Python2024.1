def media(lista):
    if len(x) >0:
        soma= 0
        for i in lista:
            soma += i
        res = soma / len(lista)
        return res
    else:
        return 0.0
def acima_valor(lista):
    valor = media(lista)
    contador = 0
    for i in lista:
        if i > valor:
            contador += 1
    return contador

def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(1, len(lista)-i):
            if lista[j-1] > lista[j]:
                # Trocar elementos se estiverem fora de ordem
                lista[j-1], lista[j] = lista[j], lista[j-1]
    return lista



entrada = input("Entrada: ")
print(f"Conteúdo em {entrada}:")
with open(entrada, 'r') as arquivo:
    texto = arquivo.read()
    print(texto)
x = texto.split()
lista = [float(num) for num in x]
print(f'Media dos numeros em {entrada}: é {media(lista)}')
print(f'Quantidade Acima de {media(lista)} em {entrada}: {acima_valor(lista)}')
ordem = ''
for i in ordenar_lista(lista):
    ordem += str(i) +" "
print(f'Ordem crescente: {ordem}')

