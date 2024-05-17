def ler(entrada):
    with open(entrada,'r') as arquivo:
        for i in arquivo:
            print(i.strip())
def maior(entrada):
    with open(entrada,'r') as arquivo:
        palavra = ''
        for i in arquivo:
            lista = i.split()
            for u in lista:
                if len(palavra) < len(u):
                    palavra = u
    return palavra
def linha(entrada):
    with open(entrada,'r') as arquivo:
        palavra = maior(entrada).lower()
        contador = 0
        vezes = []
        res = ''
        for i in arquivo:
            contador += 1
            frase = i.lower()
            if palavra in frase:
                vezes.append(contador)
        for i in vezes:
            res += str(i) + ' '
    return res
entrada = input("Arquivo: ")
ler(entrada)
print()
print(f'Palavra de Maior Comprimento: {maior(entrada)}')
print(f'Qual(is) Linha(s) Ocorreu: {linha(entrada)}')