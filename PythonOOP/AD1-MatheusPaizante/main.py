from Jogo import Jogo
class Main:
    def __init__(self):
        self.jogo = Jogo()

    def iniciar(self):
        print("Bem-vindo ao jogo de Batalha Naval!")
        self.jogo.jogar()

if __name__ == "__main__":
    main = Main()
    main.iniciar()

