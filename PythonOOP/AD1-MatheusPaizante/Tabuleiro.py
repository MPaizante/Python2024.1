class Tabuleiro:
    def __init__(self):
        self.tamanho = 10
        self.posicoes = [[' ' for i in range(self.tamanho)] for j in range(self.tamanho)]

    def inicializar_tabuleiro(self):
        self.posicoes = [[' ' for i in range(self.tamanho)] for j in range(self.tamanho)]

    def posicionar_embarcacao(self, embarcacao, linha, coluna, orientacao):
        tamanho = {'S': 1, 'P': 4, 'D': 3}[embarcacao]
        if orientacao == 'H':
            for i in range(tamanho):
                self.posicoes[linha][coluna + i] = embarcacao
        else:
            for i in range(tamanho):
                self.posicoes[linha + i][coluna] = embarcacao

    def exibir_tabuleiro(self):
        print(" " + "  ".join(map(str, range(self.tamanho))))
        for i, linha in enumerate(self.posicoes):
            print(chr(65 + i) + " " + " ".join(linha))
