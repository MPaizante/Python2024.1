entrada = input("Digite::  ").split()
entrada = [float(n) for n in entrada]

inteiro = []
flutuante = []

for i in entrada:
    if i % int(i) == 0:
        inteiro.append(int(i))
    else:
        s = f'{i:,.4f}'
        flutuante.append(s)
x = input()
with open(x,'w') as arquivo:
    for i in flutuante:
        arquivo.write(f'{i} \n')
        print()
