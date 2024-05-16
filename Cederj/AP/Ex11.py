entrada = input().split()
lista  = []
while entrada != []:
    entrada = tuple([int(n) for n in entrada])
    lista.append(entrada)
    entrada = input().split()


def ler(pontos):
    print('Listagem dos Pontos Lidos:')
    for i in pontos:
        print(i)
ler(lista)


def comparar(pontos):
    m = 0
    maior = []
    igual = []
    for i,j in pontos:
        if len(maior) == 0:
            maior = [i,j]
            m = ((i - j)**2)**0.5
        else:
            x = ((i - j)**2)**0.5
            if maior < x:
                m = 
comparar(lista)