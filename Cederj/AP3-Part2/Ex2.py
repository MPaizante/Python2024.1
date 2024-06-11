entrada = input('Frase: ')

def sem(x):
    frase = x.split()
    linha = ''
    for f in frase:
        linha += f
    return linha
espaco = sem(entrada)
print(f'A frase sem espaços é {espaco}')

def quatidade(x,y):
    consoantes = 0
    vogais = 0
    for i in y:
        if i.lower() in 'bcdfghjklmnpqrstwvxyz':
            consoantes += 1
        else:
            vogais += 1
    return f"A quantidade de vogais de '{x}' é {vogais} e a quantidade de consoantes é {consoantes} "

total = quatidade(entrada,espaco)
print(total)

def palindromo(x):
    p = x[::-1]
    if p == x:
        return f'{x} é palíndroma'
    else:
        return f'{x} não é palíndroma'
print(palindromo(espaco))