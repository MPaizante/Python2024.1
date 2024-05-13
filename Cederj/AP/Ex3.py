def distancia_pontos(x2,x1, y2,y1):
    res = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return res

entrada = input("entrada: ")
with open(entrada,'r') as aquivo:
    maior = []
    menor = []
    for i in aquivo:
        print(i.strip())
        lista = i.split()
        lista = [int(n) for n in lista]
        if len(maior) == 0:
            maior.append(lista[0])
            maior.append(lista[1])
        else:
            if lista[0] >= maior[0] and lista[1] >= maior[1]:
                maior[0] = lista[0]
                maior[1] = lista[1]
        if len(menor) == 0:
            menor.append(lista[0])
            menor.append(lista[1])
        else:
            if lista[0] <= menor[0] and lista[1] <= menor[1]:
                menor[0] = lista[0]
                menor[1] = lista[1]

    maior_t = tuple(maior)
    menor_t = tuple(menor)
    print(f'Pontos mais distantes: {menor_t} e {maior_t}')
    print(f'Distancia entre eles: {distancia_pontos(maior[0],menor[0],maior[1],menor[1]):,.1f}')

