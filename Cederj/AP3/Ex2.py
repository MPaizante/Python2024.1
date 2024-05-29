entrada = input('Digite: ').split()
def espaço(linha):
    frase = ''
    for i in linha:
        frase +=i
    return frase
sem = espaço(entrada)
print(f'A frase sem espaços é {sem}')

def quantidade(linha):
    frase = ''
    frase2= ''
    for u in linha:
        frase +=u
    for j in linha:
        frase2 += j +' '
    vogais = 0
    consoantes = 0
    for i in frase:
        if i in "aeiou" or i in 'AEIOU':
            vogais+=1
        else:
            consoantes +=1

    return f"A quantidade de vogais de '{frase2}' é {vogais} e a quantidade de consoantes é {consoantes}"
print(quantidade(entrada))


def palindromo(linha):
    frase = ''
    for i in linha:
        frase += i

    if frase[:] == frase[::-1]:
        return f'{frase} é palindroma'
    else:
        return f'{frase} não é palindroma'
print(palindromo(entrada))