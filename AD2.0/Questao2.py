ler = int(input("Quantos numeros você quer ler: "))

valor = 0
lista = []
x = 1
for x in range(1,ler+1):
    entrada = int(input(f"Digite o {x}º valor: "))
    valor += entrada
    lista.append(entrada)

lista.sort()
media =valor/len(lista)
print(f'Menor dos {ler} numeros lidos: {lista[0]}')
print(f'Maior dos {ler} numeros lidos: {lista[-1]}')
print(f'Media dos {ler} numeros lidos: {media:,.2f}')
