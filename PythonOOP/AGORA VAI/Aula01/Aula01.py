class Carro:
     velMax = 0
     ligado = False
     cor = ""
     def __init__(self, v , l , c ):
         self.velMax = v
         self.ligado = l
         self.cor = c
     def mostrar(self):
         print("---------------------------------")
         print(f"Velocidade: {self.velMax}")
         print(f"Cor: {self.cor}")
         print(f"Ligado: {('Sim' if self.ligado else 'Não')}")
         print("---------------------------------")
     def ligar(self):
         self.ligado = True
     def deligar(self):
         self.ligado = False
     def andar(self):
         if(self.ligado):
             print("Andando!")
         else:
             print("Carro desligado!")



c1 = Carro(200 , False, "Preto")
c2 = Carro(120 , False , "Branco")
c3 = Carro(350 , True, "Azul")

c1.mostrar()
c1.ligar()
c1.andar()

c2.mostrar()
c2.andar()

c3.mostrar()
c3.andar()
