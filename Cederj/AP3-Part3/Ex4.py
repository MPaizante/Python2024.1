entrada = input("Valores  >").split()
entrada = [float(n) for n in entrada]
inteiro = []
fluturante = []
for i in entrada:
    if i % int(i) == 0:
        inteiro.append(int(i))
    else:
        fluturante.append(i)
print(inteiro)
print(fluturante)
x = input('Arquivo?  ')
with open(x,'a') as arquivo:
    for i in inteiro:
        arquivo.write(f'{i}\n')
with open(x,'a') as arquivo:
    for i in fluturante:
        arquivo.write(f'{i:,.4f}\n')