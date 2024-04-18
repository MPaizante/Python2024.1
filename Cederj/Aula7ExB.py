lista = []
x = True
while True:
    n = input("Digite: ")
    if not n:
        break
    lista.append(n)
lista = [int(num) for num in lista]

maior = 0
pos = 0
for i in lista:
    if i > maior:
        maior = i
        pos = lista.index(i)
print(f'Maior numero lido foi {maior} na posição {pos+1}')

