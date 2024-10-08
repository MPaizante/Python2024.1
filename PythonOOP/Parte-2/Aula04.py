from tkinter import *


root = Tk()
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="lightgray")
        self.root.geometry("800x600")
        self.root.resizable(True,True)
        self.root.maxsize(width = 1028 , height = 780)
        self.root.minsize(width= 400, height= 300)
    def frames_da_tela(self):
        self.frames1 = Frame(self.root, bd = 4 , bg= "lightblue", highlightbackground= "blue", highlightthickness= 2)
        self.frames1.place(relx = 0.02 , rely =0.02, relwidth = 0.96, relheight = 0.46 )

        self.frames2 = Frame(self.root, bd=4, bg="lightblue", highlightbackground="blue", highlightthickness=2)
        self.frames2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.46)
    def criando_botoes(self):
        #Criando botão Limpar
        self.bt_limpar = Button(self.frames1, text= "Limpar")
        self.bt_limpar.place(relx = 0.1 , rely = 0.1 , relwidth = 0.1, relheight = 0.15 )
        # Criando botão Buscar
        self.bt_buscar = Button(self.frames1, text="Buscar")
        self.bt_buscar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Novo
        self.bt_buscar = Button(self.frames1, text="Novo")
        self.bt_buscar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Alterar
        self.bt_buscar = Button(self.frames1, text="Alterar")
        self.bt_buscar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Apagar
        self.bt_buscar = Button(self.frames1, text="Apagar")
        self.bt_buscar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)





Application()