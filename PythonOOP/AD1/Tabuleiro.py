class Tabuleiro:

    def criar_tabuleiro(self):
        matriz = [[" " for i in range(10)] for j in range(10)]
        return matriz


    def imprimir_tabuleiro(self,tabuleiro):
        self.tabuleiro = tabuleiro
        print("  " + "  ".join([str(i) for i in range(10)]))
        for idx, linha in enumerate(self.tabuleiro):
            print(str(idx) + " x" + " x".join(linha))
