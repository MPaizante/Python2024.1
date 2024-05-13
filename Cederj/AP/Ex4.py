entrada = input('Digite: ')
apostas = input('Apostas: ').split()
apostas = [int(n) for n in apostas]
seis = 0
cinco = 0
quatro = 0
tres = 0
valor = 0
with open(entrada,'r') as arquivo:
    for i in arquivo:
        x = i.split()
        x = [int(n) for n in x]
        for u in range(len(x)):
            if apostas[u] in x:
                valor += 1
        if valor == 6:
            seis +=1
        elif valor == 5:
            cinco += 1
        elif valor == 4:
            quatro += 1
        elif valor == 3:
            tres +=1
        else:
            valor = 0
        valor = 0
print(f'Com 6 acertos tivemos: {seis}\n'
      f'Com 5 acertos tivemos:{cinco}\n'
      f'Com 4 acertos tivemos:{quatro}\n'
      f'Com 3 acertos tivemos:{tres}')

