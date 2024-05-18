entrada = input('Entrada:   ').split()
maior = []
menor = []
while entrada != []:
    x = [int(n) for n in entrada]
    if len(maior) == 0 and len(menor) == 0:
        maior = tuple(x)
        menor = tuple(x)
    else:
        if maior[0] <= x[0] and maior[1] <= x[1]:
            maior = tuple(x)
        if menor[0] >= x[0] and menor[1] >= x[1]:
            menor = tuple(x)
    entrada = input().split()
def distancia(Ax,Bx,Ay,By):
    res = ((Ax-Ay)**2+(Bx-By)**2)**0.5
    return res
print(f'Pontos Mais Distantes: {menor} e {maior}')
print(f'Distância entre eles (com precisão de uma casa decimal): {distancia(menor[0],menor[1],maior[0],maior[1]):,.1f}')