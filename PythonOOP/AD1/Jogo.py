from AD1.Embarcacao import Embarcacao
from Tabuleiro import Tabuleiro
from tiro import Tiro


class Jogo:
    def __init__(self):
        tabuleiro_jogador = [[" " for i in range(10)] for j in range(10)]
        tabuleiro_computador =  [[" " for i in range(10)] for j in range(10)]
        Embarcacao(tabuleiro_computador)

        while True:
            Tabuleiro.imprimir_tabuleiro(tabuleiro_jogador)
            linha = int(input("Escolha a linha (0-9): "))
            coluna = int(input("Escolha a coluna (0-9): "))
            resultado = Tiro(tabuleiro_computador, linha, coluna)
            if resultado is None:
                print("Você já atirou aqui. Tente novamente.")
            elif resultado:
                print("Acertou!")
            else:
                print("Água!")

            if all(cell != "N" for row in tabuleiro_computador for cell in row):
                print("Parabéns! Você afundou todos os navios!")
                break
