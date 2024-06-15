d = dict()
entrada = input('Digite o nome: ')
if not entrada:
    print('Nenhuma pessoa foi inserida no dicionário!')
while entrada != '':
    des = input('Digite a descrição: ').split()
    if entrada in d:
        d[entrada] = des
    else:
        d[entrada] = des
    entrada = input('Digite o nome: ')

print('Dicionário de Pessoas Inseridas:')
matriz = list(d)
def ordena(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                lista[j] , lista[i] = lista[i] , lista[j]
    return lista
matriz_ord = ordena(matriz)

for i in matriz_ord:
    print(f'{i} {str(d[i][0])} {int(d[i][1])} {float(d[i][2])} {float(d[i][3])}')

