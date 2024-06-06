entrada = input('Aposta: ')
valores = input('Numeros: ').split()
tres = 0
quatro = 0
cinco = 0
seis = 0
with open(entrada,'r') as arquivo:
    for i in arquivo:
        linha = i.split()
        contador = 0
        for u in linha:
            if u in valores:
                contador += 1
        if contador == 6:
            seis += 1
        elif contador == 5:
            cinco += 1
        elif contador == 4 :
            quatro += 1
        elif contador == 3:
            tres += 1
        else:
            contador = 0
print('Quantidades de Apostas Premiadas:')
print(f'Com 6 acertos tivemos: {seis} aposta(s)  ')
print(f'Com 5 acertos tivemos: {cinco} aposta(s)  ')
print(f'Com 4 acertos tivemos: {quatro} aposta(s)  ')
print(f'Com 6 acertos tivemos: {tres} aposta(s)  ')