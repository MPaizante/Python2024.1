class Tiro:
    def __init__(self,tabuleiro, linha, coluna):
            if tabuleiro[linha][coluna] == "N":
                tabuleiro[linha][coluna] = "X"
                return True
            elif tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "-"
                return False
            return None