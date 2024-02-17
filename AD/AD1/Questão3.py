def programa():
    numeros = []
    while True:
        linha = input("Entrada: ")
        if not linha:
            break  
        numeros.append(float(linha))

    return numeros

def maior(numeros):
    ultimo = numeros[-1]
    maiores = [num for num in numeros if num > ultimo]

    print(f"Relação dos Números Maiores que {ultimo}")
    for numero in maiores:
        print(numero)


numeros = programa()
maior(numeros)


