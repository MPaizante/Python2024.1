entrada = input('Texto: ')
with open(entrada,'r') as arquivo:
    d = dict()
    for i in arquivo:
        frase = i.split()
        for u in frase:
            if u in d:
                d[u] += 1
            else:
                d[u] = 1


def mostraOrdenado(vals):
    valores = list(vals)
    # Ordenar Vetor por Seleção
    for i in range(len(valores) - 1):
        ondeMenor = i
        for j in range(i + 1, len(valores)):
            if valores[j] < valores[ondeMenor]:
                ondeMenor = j
        valores[i], valores[ondeMenor] = valores[ondeMenor], valores[i]
    # Mostra Ordenado
    for p in valores:
        if vals[p] == 1:
            print(p, "ocorreu", vals[p], "vez")
        else:
            print(p, "ocorreu", vals[p], "vezes")
mostraOrdenado(d)
