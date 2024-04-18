
lista = input("Digite: ").split()
n = [int(num) for num in lista]
lista = [int(num) for num in lista]

for i in range(len(lista)):
    for j in range(0, len(lista) -i -1):
        if lista[j] > lista[j+1]:
            lista[j],lista [j+1] = lista[j+1] , lista [j]
for i in lista:
    print(i)
for i in n:
    print(i)

