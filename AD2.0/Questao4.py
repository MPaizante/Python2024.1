def subprograma(numero):# subprograma para fazer a contagem
    if numero == 1:# condicao para caso o numero digitado seja 1
        return 1

    if numero == 2:# condicao para caso o numero digitado seja 2
        return 2

    anterior = 1
    atual = 2

    for x in range(3, numero + 1):#loop para caso seja 3 ou maior
        proximo = anterior + atual
        anterior = atual
        atual = proximo

    return atual

entrada = int(input("Entrada: "))#entrada para fazer a contagem


resultado = subprograma(entrada)
print(f"Posso subir a escada de {entrada} degraus de {resultado} formas")#saida
