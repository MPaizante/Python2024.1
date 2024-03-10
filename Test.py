def elementos_repetidos(sequencia):
    repetidos = set()
    elementos_vistos = set()

    for elemento in sequencia:
        if elemento in elementos_vistos:
            repetidos.add(elemento)
        else:
            elementos_vistos.add(elemento)

    return sorted(list(repetidos))


def inversao_sequencia(sequencia):
    return list(reversed(sequencia))


def inversoes_e_quantidade(sequencia):
    inversoes = 0

    for i in range(len(sequencia)):
        for j in range(i + 1, len(sequencia)):
            if sequencia[i] > sequencia[j]:
                inversoes += 1

    return inversoes, sequencia


# Leitura da sequência da entrada padrão
entrada = input("Digite a sequência de números inteiros separados por espaço: ")
sequencia = list(map(int, entrada.split()))

# a) Elementos repetidos
repetidos = elementos_repetidos(sequencia)
print("a) Elementos repetidos:", repetidos)

# b) Sequência obtida pela inversão
sequencia_invertida = inversao_sequencia(sequencia)
print("b) Sequência invertida:", sequencia_invertida)

# c) Inversões e quantidade de inversões
quantidade_inversoes, sequencia_com_inversoes = inversoes_e_quantidade(sequencia)
print("c) Inversões:", sequencia_com_inversoes)
print("   Quantidade de inversões:", quantidade_inversoes)
