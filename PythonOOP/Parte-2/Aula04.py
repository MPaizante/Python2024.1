from tkinter import *
from tkinter import ttk
import sqlite3

from test import lista

root = Tk()

class Funcs(object):
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
        print("Conectando...")
    def desconecta_bd(self):
        self.conn.close()
        print("Banco de Dados Desconectado...")
    def montarTabelas(self):
        self.conecta_bd()
        #Criando Tabela
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
        cod INTEGER PRYMARY KEY,
        nome_cliente CHAR(40) NOT NULL,
        telefone INTEGER(20),
        cidade CHAR(40)
        
        );""")
        self.conn.commit()
        print("Banco de dados Criado...")
        self.desconecta_bd()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_bd()

        self.cursor.execute("""
        INSERT INTO clientes(nome_cliente,telefone,cidade)
        VALUES(?,?,?);
        """,(self.nome,self.telefone,self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC;""")
        for i in lista:
            self.listaCli.insert(" ",END, values=i)
        self.desconecta_bd()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frames1()
        self.lista_frame2()
        self.montarTabelas()
        self.select_lista()
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
        self.bt_limpar = Button(self.frames1, text= "Limpar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'),command= self.limpa_tela)
        self.bt_limpar.place(relx = 0.2 , rely = 0.1 , relwidth = 0.1, relheight = 0.15 )
        # Criando botão Buscar
        self.bt_buscar = Button(self.frames1, text="Buscar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Novo
        self.bt_novo = Button(self.frames1, text="Novo", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'),command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Alterar
        self.bt_alterar = Button(self.frames1, text="Alterar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # Criando botão Apagar
        self.bt_apagar = Button(self.frames1, text="Apagar", bd = 3, bg = 'lightgray', fg='white', font=('verdana',8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #############Label e entrada do CODIGO!!!!!!!!!!!!!!!!!

        self.lb_codigo = Label(self.frames1, text="Código", bg='white')
        self.lb_codigo.place(relx = 0.05 , rely = 0.05)

        self.codigo_entry = Entry(self.frames1)
        self.codigo_entry.place(relx = 0.05 , rely = 0.15, relwidth = 0.1 ,relheight = 0.08)

        #############Label e entrada do NOME!!!!!!!!!!!!!!!!!
        self.lb_nome = Label(self.frames1, text="Nome", bg='white', fg= '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frames1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85, relheight=0.08)

        #############Label e entrada do Telefone!!!!!!!!!!!!!!!!!
        self.lb_telefone = Label(self.frames1, text="Telefone", bg='white', fg= '#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frames1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.08)

        #############Label e entrada do Cidade!!!!!!!!!!!!!!!!!
        self.lb_cidade = Label(self.frames1, text="Cidade", bg='white', fg= '#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frames1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.08)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frames2, height= 3, columns= ('col1','col2','col3','col4',))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigos")
        self.listaCli.heading("#2", text="Nomes")
        self.listaCli.heading("#3", text="Telefones")
        self.listaCli.heading("#4", text="Cidades")

        self.listaCli.column("#0",width= 1,)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx = 0.01, rely = 0.1, relwidth = 0.95 , relheight = 0.85)

        self.scrollLista = Scrollbar(self.frames2, orient='vertical')
        self.listaCli.configure(yscroll = self.scrollLista.set)
        self.scrollLista.place(relx = 0.96 , rely= 0.1, relwidth = 0.04, relheight = 0.85)
Application()