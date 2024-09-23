import  random
class Embarcacao:
    def __init__(self,tabuleiro):
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