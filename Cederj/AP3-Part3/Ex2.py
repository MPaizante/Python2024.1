entrada = input('Digite: ')
d = dict()
with open(entrada,'r') as arquivo:
    for i in arquivo:
        linha = i.split()
        for j in linha:
            if j in d:
                d[j] +=1
            else:
                d[j] = 1
lista = list(d)
for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[j] < lista[i]:
            lista[j],lista[i] =lista[i],lista[j]
for i in lista:
    if d[i] == 1:
        print(f'{i} ocorreu {d[i]} vez')
    else:
        print(f'{i} ocorreu {d[i]} vezes')