def contagem(x):
    cont = 0
    for letras in x:
        if letras.upper() in "AEIOU":
            cont += 1
    return cont % 2 == 0
def inverte(x):
    res = ''
    for letras in x:
        res = letras + res
    return res

def processa(frase):
    entrada = frase.split()
    for palavra in entrada:
        if contagem(palavra):
            print(palavra, end=' ')
        else:
            print(inverte(palavra), end=' ')
    return None

entrada = input()
while entrada != "":
    processa(entrada)
    print()
    entrada = input()


