entrada = input('Digite:  ')
with open(entrada,'r') as arquivo:
    matriz = []
    for i in arquivo:
        linha = i.split()
        linha = [int(n) for n in linha]
        matriz.append(linha)
maior = []
menor = []

for i in matriz:
    if len(maior) == 0 and len(menor) == 0:
        maior = i
        menor = i
    else:
        if i[0] >= maior[0] and i[1] >= maior[1]:
            maior = i
        if i[0] <= menor[0] and i[1] <= menor[1]:
            menor = i
t_maior = tuple(maior)
t_menor = tuple(menor)
print(f'Pontos Mais Distantes: {t_menor} e {t_maior}')
def distancia(ax,ay,bx,by):
    res = ((ax-bx)**2+(ay-by)**2)**0.5
    return res
dis = distancia(t_menor[0],t_menor[1],t_maior[0],t_maior[1])
print(f'Distância entre eles (com precisão de uma casa decimal): {dis:,.1f} ')