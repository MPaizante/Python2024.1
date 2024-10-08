from tkinter import *


root = Tk()
class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frames1()
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
    def widgets_frames1(self):
        #Criando botão Limpar
        self.bt_limpar = Button(self.frames1, text= "Limpar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_limpar.place(relx = 0.2 , rely = 0.1 , relwidth = 0.1, relheight = 0.15 )
        # Criando botão Buscar
        self.bt_buscar = Button(self.frames1, text="Buscar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Novo
        self.bt_buscar = Button(self.frames1, text="Novo", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_buscar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Alterar
        self.bt_buscar = Button(self.frames1, text="Alterar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_buscar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Apagar
        self.bt_buscar = Button(self.frames1, text="Apagar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_buscar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #############Label e entrada do CODIGO!!!!!!!!!!!!!!!!!

        self.lb_codigo = Label(self.frames1, text="Código")
        self.lb_codigo.place(relx = 0.05 , rely = 0.05)

        self.codigo_entry = Entry(self.frames1)
        self.codigo_entry.place(relx = 0.05 , rely = 0.15, relwidth = 0.1 ,relheight = 0.08)

        #############Label e entrada do NOME!!!!!!!!!!!!!!!!!
        self.lb_nome = Label(self.frames1, text="Nome")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frames1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85, relheight=0.08)

        #############Label e entrada do Telefone!!!!!!!!!!!!!!!!!
        self.lb_telefone = Label(self.frames1, text="Telefone")
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frames1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.08)

        #############Label e entrada do Cidade!!!!!!!!!!!!!!!!!
        self.lb_cidade = Label(self.frames1, text="Cidade")
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frames1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.08)


Application()