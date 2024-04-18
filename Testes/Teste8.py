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





def primos2(lista):
    lista_primos = []
    for i in lista:
        if i > 0:
            teste_primos =[]
            for u in range(1, i+1):
                if i % u ==0:
                    teste_primos.append(u)
            if teste_primos == 2:
                lista_primos.append(i)
