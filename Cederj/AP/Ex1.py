entrada = int(input("quantidade: "))
x = int(input("começa: "))
y = int(input("só vai: "))
soma = y
lista = []
while len(lista) < entrada:
    lista.append(soma)
    lista.append(x)
    soma += x
    x += soma
print(f'Os {entrada} elementos da sequencia são {lista}')
par = []
for i in lista:
    if i % 2 ==0:
        par.append(i)
print(f'Os elementos pares da sequência são {par}.')
quadrado = []
for i in range(len(lista)):
            for j in range(2, int(lista[i])):
                if j**2 == lista[i]:
                    quadrado.append(lista[i])
print(f'Dentre esses, os que são quadrado perfeito são {quadrado}.')