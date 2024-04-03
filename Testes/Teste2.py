def palindromo(x):
    lista = []
    for i in x:
        lista.append(i)
    if lista[0] == lista[-1]:
        return print(x)

loop = True
entrada = input("Digite: ")
while (loop):
    palindromo(entrada)
    entrada = input("Digite: ")
    if not entrada:
        loop = False
    print()