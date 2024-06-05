entrada = input("Digite:------")
if not entrada:
    print('Nenhuma pessoa foi inserida no dicionário!')
else:
    lista = dict()
    while entrada != '':
        entrada2 = input("Digite: ").split()
        lista[entrada] = entrada2
        entrada = input("Digite:------")
    print('Dicionário de Pessoas Inseridas:')
    for i in sorted(lista):
        print(f'{i} {lista[i][0]} {lista[i][1]} {lista[i][2]} {lista[i][3]}')

