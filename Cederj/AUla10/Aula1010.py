def primo(x):
    if x <= 2:
        return True
    else:
        for i in range(2,x):
            if x % i==0:
                return False
        return True

primos = set()
n_primos = set()
numero = input("Digite: ")
while numero!='':
    res = primo(int(numero))
    if res:
        print(f'O numero {numero} é primo')
        primos.add(int(numero))
    else:
        print(f'O numero {numero} não é primo')
        n_primos.add(int(numero))
    numero = input("Digite: ")
print(f'Numero não primos {n_primos}')
print(f'Numeros primos {primos}')
