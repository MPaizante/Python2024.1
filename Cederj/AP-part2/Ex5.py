d = {}
entrada = input('Digite: ')
while entrada != '':
    linha = input('Linha: ').split()
    #linha = [float(n) for n in linha]
    if entrada in d:
        d[entrada] = linha
    else:
        d[entrada] = linha
    entrada = input('Digite: ')

if len(d) == 0:
    print('Nenhuma pessoa foi inserida no dicionário!')
else:
    print('Dicionário de Pessoas Inseridas:')
    for i in d:
        print(f'{str(i)} {str(d[i][0])} {int(d[i][1])} {float(d[i][2])} {float(d[i][3])}')
