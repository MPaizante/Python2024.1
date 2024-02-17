n = int(input("Quantos numeros você quer ler: "))

v = 0
y = []
for x in range(n):
    entrada = int(input("Digite os valores: "))
    v += entrada
    y.append(entrada)

lista = sorted(y)
t =v/len(lista)
print(f'Menor dos {n} numeros lidos: {lista[0]}')
print(f'Maior dos {n} numeros lidos: {lista[-1]}')
print(f'Media dos {n} numeros lidos: {t:,.2f}')
