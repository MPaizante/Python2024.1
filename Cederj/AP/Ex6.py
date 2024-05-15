entrada = input()
with open(entrada,'r') as arquivo:
    valor = 0
    c = 0
    for i in arquivo:
        lista = i.split()
        lista1 = [float(num) for num in lista]
        for u in lista1:
            valor += u
            c += 1
    media = valor/c
    print(media)
with open(entrada,'r') as arquivo:
    acima = []
    for i in arquivo:
        lista = i.split()
        lista1 = [float(num) for num in lista]
        for u in lista1:
            if u > media:
                acima.append(u)
    print(f'A quantidade acima da media é {len(acima)}')