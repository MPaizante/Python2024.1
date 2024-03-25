entrada = input('Digite o vogal: ').upper()
lista = []
while True:
    linha = input('Digite a sua frase: ').upper().split()
    if not linha:
        break
    lista.append(linha)
c = 0
lista2=[]
for i in lista:
    for u in i:
        if u[0] == entrada or u[-1] == entrada:
            c +=1
            lista2.append(u)
for y in lista2:
    print(y)
print(f'Iniciadas ou Finalizadas pelo Caracter {entrada} = {c} Vez(es)')



