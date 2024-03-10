def subprograma():
    lista = []
    while True:
        linha = input("Entrada: ")
        if not linha:
            break
        lista.append(float(linha))

    return lista

def maior(numeros):
    ultimo = numeros[-1]
    maiores = [num for num in numeros if num > ultimo]
    print(f"Relação dos Números Maiores que {ultimo}:")
    for maior in maiores:
        print(maior)

numeros = subprograma()
maior_numero = maior(numeros)


