def programa(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    anterior =1
    atual =2

    for x in range(3, n + 1):
        proximo = anterior + atual
        anterior= atual
        atual = proximo

    return atual

entrada = int(input("Entrada: "))


resultado = programa(entrada)
print(f"Posso subir a escada de {entrada} degraus de {resultado} formas")
