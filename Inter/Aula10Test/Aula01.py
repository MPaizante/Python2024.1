def sal(x):
    if x <= 400:
        y = x * 0.15
        x = x + y
        return x
    elif x <= 800:
        y = x * 0.12
        x = x + y
        return x
    elif x <= 1200:
        y = x * 0.10
        x = x + y
        return x
    elif x <= 2000:
        y = x * 0.07
        x = x + y
        return x
    else:
        y = x * 0.04
        x = x + y
        return x
def retorno(x):
    if x <= 400:
        y = x * 0.15
        return y
    elif x <= 800:
        y = x * 0.12
        return y
    elif x <= 1200:
        y = x * 0.10
        return y
    elif x <= 2000:
        y = x * 0.07
        return y
    else:
        y = x * 0.04
        return y

def porcentagem(x):
    if x <= 400:
        return int(100*0.15)
    elif x <= 800:
        return int(100*0.12)
    elif x <= 1200:
        return int(100*0.10)
    elif x <= 2000:
        return int(100*0.07)
    else:
        return int(100*0.04)

print('Digite o salario abaixo!')
salario = float(input('Salario: '))

print(f'Novo salario: {sal(salario):,.2f}')
print(f'Reajuste ganho: {retorno(salario):,.2f}')
print(f'Em percentual: {porcentagem(salario):,.0f}%')