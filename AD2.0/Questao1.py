entrada = str(input("Entrada: ").upper()) #entrada onde sera inserido a letra desejada
lista = []
while True: #loop onde será obtido os textos
    texto = str(input("Texto: ").upper())
    if not texto: #condicao para parar o texto
        break
    texto = texto.split()
    lista += texto


cont = 0
for x in lista: #loop para percorrer a lista e checar a primeira e ultima letra de cada palavra
    if (x[0] == entrada or x[-1] == entrada):
        print(x)
        cont += 1

print(f'Iniciadas ou Finalizadas pelo Caractere {entrada} = {cont} Vez(es)') #Saida