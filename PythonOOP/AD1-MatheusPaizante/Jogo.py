from Tabuleiro import Tabuleiro
from Jogador import Jogador
import random

class Jogo:
    def __init__(self):
        self.jogadores = [Jogador("Jogador 1"), Jogador("Jogador 2")]
        self.tabuleiros = [Tabuleiro(), Tabuleiro()]
        self.jogador_atual = 0

    def gerar_tabuleiro(self):
        for tabuleiro in self.tabuleiros:
            tabuleiro.inicializar_tabuleiro()

    def exibir_tabuleiro(self, jogador):
        self.tabuleiros[jogador].exibir_tabuleiro()

    def criar_jogadores(self):
        for jogador in self.jogadores:
            jogador.posicionar_embarcacoes()

    def verificar_jogada(self, linha, coluna):
        if 0 <= linha < 10 and 0 <= coluna < 10:
            return True
        return False

    def fazer_jogada(self, linha, coluna):
        tabuleiro_adversario = self.tabuleiros[1 - self.jogador_atual]
        if tabuleiro_adversario.posicoes[linha][coluna] == ' ':
            tabuleiro_adversario.posicoes[linha][coluna] = 'o'
            return 'erro'
        elif tabuleiro_adversario.posicoes[linha][coluna] in ['S', 'P', 'D']:
            tabuleiro_adversario.posicoes[linha][coluna] = 'x'
            return 'acerto'
        return 'repetido'

    def jogar(self):
        self.gerar_tabuleiro()
        self.criar_jogadores()
        while True:
            jogador = self.jogadores[self.jogador_atual]
            print(f"\nTurno de {jogador.nome}")
            self.exibir_tabuleiro(1 - self.jogador_atual)
            linha, coluna = jogador.inserir_jogada()
            if self.verificar_jogada(linha, coluna):
                resultado = self.fazer_jogada(linha, coluna)
                if resultado == 'acerto':
                    print("Acertou!")
                elif resultado == 'erro':
                    print("Errou!")
                else:
                    print("Jogada repetida!")
                if self.verificar_vitoria():
                    print(f"{jogador.nome} venceu!")
                self.jogador_atual = 1 - self.jogador_atual
            else:
                print("Jogada inválida. Tente novamente.")

    def verificar_vitoria(self):
        tabuleiro_adversario = self.tabuleiros[1 - self.jogador_atual]
        for linha in tabuleiro_adversario.posicoes:
            if any(pos in ['S', 'P', 'D'] for pos in linha):
                return False
        return True
