entrada = input('Entrada:  ')
aposta = input('Apsota: ').split()
s = 0
c = 0
q = 0
t = 0
with open(entrada,'r') as arquivo:
    print(f'Conteúdo do Arquivo {entrada}:')
    for i in arquivo:
        contador = 0
        linha = i.split()
        for j in linha:
            if j in aposta:
                contador += 1
        if contador == 6:
            s += 1
        elif contador == 5:
            c += 1
        elif contador == 4:
            q +=1
        elif contador == 3:
            t += 1
        else:
            contador = 0
print('Quantidades de Apostas Premiadas:')
print(f'Com 6 acertos tivemos: {s} aposta(s)')
print(f'Com 5 acertos tivemos: {c} aposta(s)')
print(f'Com 4 acertos tivemos: {q} aposta(s)')
print(f'Com 3 acertos tivemos: {t} aposta(s)')