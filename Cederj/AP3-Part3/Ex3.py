entrada = int(input('Digite: '))

def binario(numero):
    valor = numero // 2
    if numero == 1:
        res = numero % 2
        print(f'{res}', end='')
        return None
    res = numero % 2
    print(f'{res}',end='')
    binario(valor)

valor = binario(entrada)

print(valor)


