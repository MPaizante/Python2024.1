print(int("100"))
print(int("100", 10))   # same thing, 10 is the default value for the base
print(int("100", 8))     # now the base is 8, so the result is 1*64 = 64


def str_mult(x,y = 3):
    return  x * y

print('-'*31, 'palavra chave', '-'*31)

'''names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print(f'Nome: {name}')
    v =1
    for score in scores:
        print(f'{v}º Score: {score}')
        v += 1

lista = []
x = input("Nome: ")
while x !='':
    L = []
    L.append(x)
    y = input("Valor: ")
    c = []
    while y != '':
        b = int(y)
        c.append(b)
        y = input("Valor: ")
    L.append(c)
    lista.append(tuple(L))
    x = input("Nome: ")

print(lista)'''

T = [('a', [1,2,3]), ('b', [2,1,2]), ('c', [3,4,5])]
for i,k in T:
    print(i)
    for u in range(len(k)):
        print(k[u])
