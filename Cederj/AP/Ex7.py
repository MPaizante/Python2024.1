def ler(x):
    print(f'Conteudo de {x}:')
    with open(x,'r') as arquivo:
        for i in arquivo:
            print(i.strip())
def maior(x):
    with open(x,'r') as arquivo:
        palavra = ''
        for i in arquivo:
            lista = i.split()
            for u in lista:
                if len(u) > len(palavra):
                    palavra = u
    return palavra

def ocorrencia(x,y):
    with open(x,'r') as arquivo:
        contador = 0
        linha = []
        for i in arquivo:
            contador += 1
            lista = i.split()
            for u in lista:
                if u == y:
                    linha.append(contador)
                    break
        vezes =''
        for i in linha:
            vezes += str(i) + ' '
        return vezes

entrada = input('Entrada: ')
ler(entrada)
palavra = maior(entrada)
print(f'Palavra de Maior Comprimento: {palavra}')

print(f'Qual(is) Linha(s) Ocorreu: {ocorrencia(entrada,palavra)}')