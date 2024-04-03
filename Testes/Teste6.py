lista = []
entrada = input("Digite o valor: ")
while (entrada !=""):
    lista.append(entrada)
    entrada = input("Digite o valor: ")

lista = [int(num) for num in lista]

def pares(lista):
    lista_pares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
    if len(lista_pares)> 0:
        return lista_pares
    return
def impares(lista):
    lista_impares = []
    for i in lista:
        if i % 2 == 1:
            lista_impares.append(i)
    if len(lista_impares)>0:
        return lista_impares
    return

def primos(lista):
    lista_primos = []
    for i in lista:
        if i > 0:
            teste_primo = []
            for u in range(1,i+1):
                if i % u == 0:
                    teste_primo.append(u)
            if len(teste_primo) == 2:
                lista_primos.append(i)

    return lista_primos

print("Listagem de pares:")
lista_pares = pares(lista)
for i in lista_pares:
    print(i)

print("Fim da lista Pares")

print("Lista de impares:")
lista_impares = impares(lista)
for i in lista_impares:
    print(i)
print("Fim dos impares")

print("Lista primos:")
lista_primos = primos(lista)
for i in lista_primos:
    print(i)
print("Fim lista primos")
