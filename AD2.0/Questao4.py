def programa(numero):
    if numero == 1:
        return 1

    if numero == 2:
        return 2

    anterior = 1
    atual = 2

    for x in range(3, numero + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo

    return atual

entrada = int(input("Entrada: "))


resultado = programa(entrada)
print(f"Posso subir a escada de {entrada} degraus de {resultado} formas")
