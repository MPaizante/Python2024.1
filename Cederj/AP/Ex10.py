def ler(entrada):
    with open(entrada,'r') as arquivo:
        print(f'Conteúdo do Arquivo {entrada}:')
        for i in arquivo:
            print(i.strip())
        return None
def maior(entrada):
    with open(entrada,'r') as arquivo:
        palavra = ''
        for i in arquivo:
            linha = i.split()
            for u in linha:
                if len(palavra) < len(u):
                    palavra = u
        return palavra

def repete(entrada):
    with open(entrada, 'r') as arquivo:
        palavra = maior(entrada)
        paragrafo = 0
        aparece = []
        for i in arquivo:
            paragrafo +=1
            if palavra in i:
                aparece.append(paragrafo)
        linha = ''
        if len(aparece)> 0:
            for u in aparece:
                linha += str(u) + ' '
        else:
            return 'Nenhuma'
        return linha

conteudo = input()
ler(conteudo)
print(f'Palavra de Maior Comprimento: {maior(conteudo)}')
print(f'Qual(is) Linha(s) Ocorreu:{repete(conteudo)}')