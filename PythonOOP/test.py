lista = [1,23,5,8,4,55]

while True:
    for i in lista:
        print(i, end=' ')
    print()
    if len(lista)> 0:
        lista.pop(len(lista) - len(lista))
    else:
        print("underflow")
        print(lista)
        break
