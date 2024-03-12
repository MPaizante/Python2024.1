def subprograma():#subprograma pegar numeros
    lista = []
    while True:#loop para  para digitar numeros
        linha = input("Entrada: ")
        if not linha:#condicao para parar loop
            break
        lista.append(float(linha))

    return lista

def maior(numeros):#subprograma para fazer a relacao dos maiores numeros em relaçao ao ultimo numero digitado
    ultimo = numeros[-1]
    maiores = [num for num in numeros if num > ultimo]
    print(f"Relação dos Números Maiores que {ultimo}:")#saida
    for maior in maiores:
        print(maior)#saida

numeros = subprograma()
maior_numero = maior(numeros)


