entrada = str(input("Entrada: ").upper())
frases = int(input("Quantas frases você quer botar? :"))
lista = []
for y in range(frases):
    texto = str(input("Texto: ").upper())
    texto = texto.split()
    lista += texto 


n = 0
for x in lista:
    if (x[0] == entrada or x[-1] == entrada):
        print(x)
        n += 1

print(f'Iniciadas ou Finalizadas pelo Caractere {entrada} = {n} Vez(es)')