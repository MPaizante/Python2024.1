ler = int(input("Quantos numeros você quer ler: "))# entrada de um numero inteiro

valor = 0
lista = []
for x in range(1,ler+1):#loop com o numero obtido atraves da entrada 'ler'
    entrada = int(input(f"Digite o {x}º valor: "))#entrada dos numeros digitados que voce quer conferir
    valor += entrada
    lista.append(entrada)

lista.sort()#Faz com que organize a lista do maior para o menor
media =valor/len(lista)#acha a media da lista
print(f'Menor dos {ler} numeros lidos: {lista[0]}')
print(f'Maior dos {ler} numeros lidos: {lista[-1]}')
print(f'Media dos {ler} numeros lidos: {media:,.2f}')
