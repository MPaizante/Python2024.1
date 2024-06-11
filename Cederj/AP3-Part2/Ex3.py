entrada = input('Entrada:  ')
with open(entrada,'r') as arquivo:
    maior = []
    menor = []
    for i in arquivo:
        inteiro = i.split()
        inteiro = [int(n) for n in inteiro]
        if len(maior) == 0 and len(menor) == 0:
            maior = inteiro
            menor = inteiro
        else:
            if inteiro[0] >= maior[0] and inteiro[1] >= maior[1]:
                maior = inteiro
            if inteiro[0] <= menor[0] and inteiro[1] <= menor[1]:
                menor = inteiro
t_maior = tuple(maior)
t_menor = tuple(menor)
print(f'Os pontos mais distantes: {t_menor} e {t_maior}')
def distancia(Ax,Bx,Ay,By):
    d = ((Ax-Ay)**2 + (Bx-By)**2)**0.5
    return d
print(f'Distância entre eles (com precisão de uma casa decimal): {distancia(maior[0],maior[1],menor[0],menor[1]):,.1f}')