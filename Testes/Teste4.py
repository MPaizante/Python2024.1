def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(1, len(lista)-i):
            if lista[j-1] > lista[j]:
                # Trocar elementos se estiverem fora de ordem
                lista[j-1], lista[j] = lista[j], lista[j-1]
    return lista


print(ordenar_lista([1,8,5]))