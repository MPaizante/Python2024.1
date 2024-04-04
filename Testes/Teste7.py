lista = []
entrada = input()
if not entrada:
    print("Nenhum voto ocorreu!")
while (entrada != ""):
    lista.append(entrada)
    entrada = input()

votos = [0]*10


