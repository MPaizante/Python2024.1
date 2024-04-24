ano = {'j','f','m','a','ma','jn','jl','ag','s','o','n','d'}
ferias_f = {'j','f','d'}
ferias_m = {'jl'}
ferias = ferias_f.union(ferias_m)
print(ferias)
letivo = ano.difference(ferias)
print(f'Periodo letivo é {letivo}')

def conta(x):
    vogais = {'a','e','i','o','u','A','E','I','O','U'}
    v =0
    c =0
    for letras in x:
        if letras in vogais:
            v +=1
        else:
            c += 1
    print(f'Numero de vogais é {v}')
    print(f'Numero de consoantes {c}')
    return None
frase = input("Digite a frase: ")
conta(frase)