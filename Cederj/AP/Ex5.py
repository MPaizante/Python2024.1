entrada = input('Digite: ')
tamanho = input().split()
tamanho = [int(n) for n in tamanho]
palavras = {}
with open(entrada,'r') as arquivo:
    for i in arquivo:
        print(i.strip())
        frase = i.replace(',', ' ').split()
        for u in frase:
            if len(u) >= tamanho[0] and len(u) <= tamanho[1]:
                if u in palavras or u.upper() in palavras:
                    palavras[u.upper()] = palavras[u.upper()] + 1
                else:
                    palavras[u.upper()] = 1

for i in sorted(palavras):
    print(f'{i} ocorreu {palavras[i]} vez')

