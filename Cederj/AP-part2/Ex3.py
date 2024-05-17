def produz(entrada):
    valores = {}
    with open(entrada,'r') as arquivo:
        for i in arquivo:
            linha = i.split()
            for u in linha:
                if u.lower() in valores:
                    valores[u.lower()] += 1
                else:
                    valores[u.lower()] = 1
    return valores
def ordena(entrada):
    valores = produz(entrada)
    for i in range(len(valores) - 1):
        posMenor = i  # Seleciona
        for j in range(i + 1, len(valores)):  # Seleciona
            if valores[j] < valores[posMenor]:  # Seleciona
                posMenor = j  # Seleciona
        valores[i], valores[posMenor] = valores[posMenor], valores[i]
    return None

entrada = input()
print(produz(entrada))
ordena(entrada)