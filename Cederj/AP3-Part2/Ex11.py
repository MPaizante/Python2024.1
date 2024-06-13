entrada = input('Digite????????????????????????')
matriz = []
with open(entrada,'r') as arquivo:
    for i in arquivo:
        linha = i.split()
        linha = [int(n) for n in linha]
        matriz.append(linha)
menor = []
maior = []

for i in matriz:
    if len(menor) == 0 and len(maior) == 0:
        menor = i
        maior = i
    else:
        if maior[0] <= i[0] and maior[1] <= i[1]:
            maior = i
        if menor[0] >= i[0] and menor[1] >= i[1]:
            menor = i
maior_t = tuple(maior)
menor_t = tuple(menor)
print(f'Pontos Mais Distantes: {menor_t} e {maior_t}')
def distancia(ax,ay,bx,by):
    res = ((bx-ax)**2+(by-ay)**2)**0.5
    return res
dis = distancia(menor[0],menor[1],maior[0],maior[1])
print(f'Distância entre eles (com precisão de uma casa decimal): {dis:,.1f}')