entrada = input('Entrada:  ')
maior = [0,0]
menor = [0,0]
with open(entrada,'r') as arquivo:
    for i in arquivo:
        x = i.split()
        inteiro = [int(num) for num in x]
        if maior[0] == 0 and maior[1] == 0:
            maior = [inteiro[0],inteiro[1]]
            menor = [inteiro[0], inteiro[1]]
        else:
            if maior[0] <= inteiro[0] and maior[1] <= inteiro[1]:
                    maior[0] = inteiro[0]
                    maior[1] = inteiro[1]
            if menor[0] >= inteiro[0] and menor[1] >= inteiro[1]:
                    menor[0] = inteiro[0]
                    menor[1] = inteiro[1]
maior_tuple = tuple(maior)
menor_tuple = tuple(menor)
print(f'Os pontos mais distantes são: {menor_tuple} e {maior_tuple}')
def distancia(Ax,Bx,Ay,By):
    res = ((Ay-Ax)**2+(By-Bx)**2)**0.5
    return f'A Distância entre eles (com precisão de uma casa decimal): {res:,.1f}'
print(distancia(menor[0],menor[1],maior[0],maior[1]))

