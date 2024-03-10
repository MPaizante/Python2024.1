entrada = str(input("Entrada: ").upper())
lista = []
while True:
    texto = str(input("Texto: ").upper())
    if not texto:
        break
    texto = texto.split()
    lista += texto


cont = 0
for x in lista:
    if (x[0] == entrada or x[-1] == entrada):
        print(x)
        cont += 1

print(f'Iniciadas ou Finalizadas pelo Caractere {entrada} = {cont} Vez(es)')