def espaco(x):
    sem = ''
    for i in x.split():
        sem += i
    return sem
def vogais(x):
    entrada = espaco(x)
    v = 0
    c = 0
    for i in entrada:
        if i in 'aeiou' or i in 'AEIOU':
            v +=1
        else:
            c +=1
    res = f'{v} e a quantidade de consoantes é {c}'
    return res
def palindromo (x):
    entrada = espaco(x)
    res = False
    inverso = entrada[::-1]

    if inverso == entrada:
        res = True
    return res
entrada = input("Digite: ")
print(f'A frase sem espaços é {espaco(entrada)}')
print(f"A quantidade de vogais de '{entrada}' é {vogais(entrada)}")
print(f'{entrada} é palindromo {palindromo(entrada)}')

aaaa = [1,2,3,4,5]
print(aaaa[::-1])


