def ler(entrada):
    with open(entrada,'r') as arquivo:
        print(f'Conteúdo em {entrada}:')
        for i in arquivo:
            print(i.strip())
        return None
def media(entrada):
    with open(entrada,'r') as arquivo:
        contador = 0
        valores = 0
        for i in arquivo:
            linha = i.split()
            linha_float = [float(num) for num in linha]
            for u in linha_float:
                contador += 1
                valores += u
        media = valores/contador

        return media
def acima(entrada):
    with open(entrada,'r') as arquivo:
        maior = 0
        for i in arquivo:
            linha = i.split()
            linha_float = [float(num) for num in linha]
            for u in linha_float:
                if u >media(entrada) :
                    maior +=1
        return maior

conteudo = input()
ler(conteudo)
print()
print(f'Média dos Números em {conteudo}: {media(conteudo)}')
print(f'Quantidade Acima de {media(conteudo)} em {conteudo}: {acima(conteudo)} ')




