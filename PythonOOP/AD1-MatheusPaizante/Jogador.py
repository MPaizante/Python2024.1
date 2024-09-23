from Tabuleiro import Tabuleiro
import random
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.tabuleiro = Tabuleiro()

    def inserir_jogada(self):
        linha = int(input("Digite a linha (0-9): "))
        coluna = int(input("Digite a coluna (0-9): "))
        return linha, coluna

    def posicionar_embarcacoes(self):
        embarcacoes = [('S', 4), ('P', 1), ('D', 2)]
        for embarcacao, quantidade in embarcacoes:
            for _ in range(quantidade):
                while True:
                    linha = random.randint(0, 9)
                    coluna = random.randint(0, 9)
                    orientacao = random.choice(['H', 'V'])
                    if self.verificar_posicionamento(embarcacao, linha, coluna, orientacao):
                        self.tabuleiro.posicionar_embarcacao(embarcacao, linha, coluna, orientacao)
                        break

    def verificar_posicionamento(self, embarcacao, linha, coluna, orientacao):
        tamanho = {'S': 1, 'P': 4, 'D': 3}[embarcacao]
        if orientacao == 'H':
            if coluna + tamanho > 10:
                return False
            for i in range(tamanho):
                if self.tabuleiro.posicoes[linha][coluna + i] != ' ':
                    return False
        else:
            if linha + tamanho > 10:
                return False
            for i in range(tamanho):
                if self.tabuleiro.posicoes[linha + i][coluna] != ' ':
                    return False
        return True




