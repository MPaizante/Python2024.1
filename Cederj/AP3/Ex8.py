entrada = int(input('Entrada: '))
valor= int(input('Valor: '))
pulo = int(input('Pulo: '))
lista = []
while True:
    if len(lista) == entrada:
        break
    else:
        lista.append(valor)
        valor += pulo
    if len(lista) == entrada:
        break
    else:
        lista.append(pulo)
        pulo += valor
def par(lista):
    if len(lista)>0:
        lista_par = []
        for i in lista:
            if i % 2 == 0:
                lista_par.append(i)
        if len(lista_par) >0:
            return lista_par
        else:
            return f'Não há elemento par quadrado perfeito.'
    return None
def quadrado(lista):
    if len(lista)>0:
        lista_quadrado = []
        for i in lista:
            for u in range(2,i):
                if i / u == u:
                    lista_quadrado.append(i)
        if len(lista_quadrado)>0:
            return lista_quadrado
        else:
            return f'Não há elementos pares na sequência até a posição {len(lista)}'
    return None

print(f'Os 12 elementos da sequência são {lista}')
print(f'Os elementos pares da sequência são {par(lista)}')
print(f'Dentre esses, os que são quadrado perfeito são {quadrado(lista)}')

