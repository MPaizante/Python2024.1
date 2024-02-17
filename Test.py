def ler_numeros():
    numeros = []
    while True:
        linha = input("Digite um número (ou pressione Enter para encerrar): ")
        if not linha:
            break  # Encerra o loop quando uma linha vazia for digitada
        try:
            numero = float(linha)
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")

    return numeros

def numeros_maiores_que_ultimo(numeros):
    if not numeros:
        print("Nenhum número foi inserido.")
        return

    ultimo_numero = numeros[-1]
    numeros_maiores = [num for num in numeros if num > ultimo_numero]

    print("Números maiores que o último número lido:")
    for numero in numeros_maiores:
        print(numero)

# Programa principal
numeros = ler_numeros()
numeros_maiores_que_ultimo(numeros)
