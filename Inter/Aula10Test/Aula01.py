def palindromo(x):
    entrada = x.lower().replace(' ', ' ')
    return entrada == entrada[::-1]


frase = input("digite: ")
print(f'Esses são palindromos {palindromo(frase)}')
