def ler_arquivo(nome_arquivo):
    apostadores = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split('#')
            nome = dados[0]
            numeros = set(map(int, dados[1:]))
            apostadores[nome] = numeros
    return apostadores

def verificar_acertos(apostadores, numeros_sorteados):

    acertadores = {8: set(), 7: set(), 6: set(), 5: set(), 4: set(), 3: set()}
    for nome, numeros_apostados in apostadores.items():
        acertos = len(numeros_apostados.intersection(numeros_sorteados))
        acertadores[acertos].add(nome)
    return acertadores
def main():
    nome_arquivo = input("Digite o nome do arquivo de apostas: ")
    numeros_sorteados = set(map(int, input("Digite os números sorteados separados por espaço: ").split()))
    apostadores = ler_arquivo(nome_arquivo)
    if not apostadores:
        print("Nenhuma Aposta!!!")
        return
    acertadores = verificar_acertos(apostadores, numeros_sorteados)
    total_apostas = len(apostadores)
    print("Total de apostas:", total_apostas)
    for acertos in range(8, 2, -1):
        if acertadores[acertos]:
            print(f"{acertos} acertos:", sorted(acertadores[acertos]))
        else:
            print(f"{acertos} acertos: Nenhum acertador")
    if not any(acertadores.values()):
        print("ACUMULOU TUDO")

if __name__ == "__main__":
    main()
