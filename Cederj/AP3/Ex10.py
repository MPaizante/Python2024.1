

def sem(frase):
    if len(frase)>0:
        espaco = ''
        linha = frase.split()
        for i in linha:
            espaco +=i
        return espaco
    else:
        return None
def quantidade(frase):
    if len(frase)>0:
        vogais = 0
        consoantes = 0
        linha = sem(frase)
        for i in linha:
            if i.lower() in 'bcdfghjklmnpqrstvwxyz':
                consoantes +=1
            else:
                vogais += 1
        return f"A quantidade de vogais de '{frase} é {vogais} e a quantidade de consoantes é {consoantes}"
    else:
        return None
def palindroma(frase):
    if len(frase)> 0:
        linha = sem(frase)
        inverso = linha[::-1]
        if linha == inverso:
            res = f'{linha} é palíndroma'
        else:
            res = f'{linha} não é palíndroma'
        return res
    else:
        return None

entrada = input('Entrada:  ')
sem_espaco = sem(entrada)
quantidades = quantidade(entrada)
pali = palindroma(entrada)
print(f'A frase sem espaços é {sem_espaco}')
print(quantidades)
print(pali)