
lista = [9,5,8,1,2,3]
lista1=[1,2,3,4,6,5]

for i in range(len(lista)):
        for j in range(1, len(lista)-i):
            if lista[j-1] > lista[j]:
                # Trocar elementos se estiverem fora de ordem
                lista[j-1], lista[j] = lista[j], lista[j-1]
print(lista)
print(lista1[::-1])