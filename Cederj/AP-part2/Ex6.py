entrada = input('Frase: ')
lista = entrada.split()
sem =''
for i in lista:
    sem += i
print(f'A frase sem espaços é {sem}')
vogais = 0
consoantes = 0
x = 'bcdfghjklmnpqrstvwxyz'.lower() + 'bcdfghjklmnpqrstvwxyz'.upper()
print(x)
for i in sem:
    if i in x:
        consoantes += 1
    else:
        vogais += 1
print(f"A quantidade de vogais de '{entrada}' é {vogais} e a quantidade de consoantes é {consoantes}")
if sem[::] == sem[::-1]:
    print(f'{sem} é palíndroma')
else:
    print(f'{sem} não é palíndroma')