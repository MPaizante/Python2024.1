import random

# Função para criar o tabuleiro vazio
def criar_tabuleiro():
    return [[" " for i in range(10)] for j in range(10)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print("  " + "  ".join([str(i) for i in range(10)]))
    for idx, linha in enumerate(tabuleiro):
        print(str(idx) + " x" + " x".join(linha))

# Função para posicionar navios no tabuleiro
def posicionar_navios(tabuleiro):
    tamanhos_navios = [5, 4, 3, 3, 2]
    for tamanho in tamanhos_navios:
        while True:
            orientacao = random.choice(["H", "V"])
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if orientacao == "H":
                if coluna + tamanho <= 10 and all(tabuleiro[linha][coluna + i] == " " for i in range(tamanho)):
                    for i in range(tamanho):
                        tabuleiro[linha][coluna + i] = "N"
                    break
            else:
                if linha + tamanho <= 10 and all(tabuleiro[linha + i][coluna] == " " for i in range(tamanho)):
                    for i in range(tamanho):
                        tabuleiro[linha + i][coluna] = "N"
                    break

# Função para verificar se o tiro acertou um navio
def verificar_tiro(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == "N":
        tabuleiro[linha][coluna] = "X"
        return True
    elif tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = "-"
        return False
    return None

# Função principal do jogo
def batalha_naval():
    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()
    posicionar_navios(tabuleiro_computador)

    while True:
        imprimir_tabuleiro(tabuleiro_jogador)
        linha = int(input("Escolha a linha (0-9): "))
        coluna = int(input("Escolha a coluna (0-9): "))
        resultado = verificar_tiro(tabuleiro_computador, linha, coluna)
        if resultado is None:
            print("Você já atirou aqui. Tente novamente.")
        elif resultado:
            print("Acertou!")
        else:
            print("Água!")

        if all(cell != "N" for row in tabuleiro_computador for cell in row):
            print("Parabéns! Você afundou todos os navios!")
            break

# Inicia o jogo
batalha_naval()
