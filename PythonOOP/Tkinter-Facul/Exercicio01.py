from tkinter import *
from tkinter import ttk
import sqlite3
root = Tk()

class Funcs():
    def limpa_cliente(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.fone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
        print("Conectando Banco de Dados.....")
    def desconecta_bd(self):
        self.conn.close()
        print("Desconecta Banco de Dados")
    def montaTabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes ( cod INTEGER PRIMARY KEY, nome_cliente CHAR(40) NOT NULL, telefone INTEGER(20), cidade CHAR(40));
        """)
        self.conn.commit()
        print("Banco de Dados Criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""
        INSERT INTO clientes ( nome_cliente, telefone, cidade )
        VALUES( ? , ? , ?);
        """, (self.nome,self.fone,self.cidade))

        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaCli.insert("",END, values = i)
        self.desconecta_bd()
    def OnDoubleClick(self):
        self.limpa_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1 , col2, col3, col4 =  self.listaCli.item(n , 'values')
            self.codigo_entry.insert(END, col)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END,col3)
            self.cidade_entry.insert(END,col4)
    def deleta_cliente(self,event):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""",(self.codigo))
        self.conn.commit()


        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()



class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()

        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= 'lightblue')
        self.root.geometry("1200x900")
        self.root.resizable(True, True)

    def frames_da_tela(self):
        self.frame_1  = Frame(self.root, bd = 4 , bg= 'lightgray', highlightbackground="white",highlightthickness= 2)
        self.frame_1.place(relx= 0.02 ,rely = 0.02 , relwidth = 0.96 , relheight = 0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='lightgray', highlightbackground="white", highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        #Botão Limpar
        self.bt_limpar = Button(self.frame_1 , text="Limpar", bd= 3, bg='#4285f4',fg='white',font=('times new roman',12,'bold'),command= self.limpa_cliente)
        self.bt_limpar.place(relx = 0.2, rely = 0.1 , relwidth = 0.1 , relheight = 0.15)

        # Botão Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd= 3, bg='#4285f4',fg='white',font=('times new roman',12,'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd= 3, bg='#4285f4',fg='white',font=('times new roman',12,'bold'),command= self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd= 3, bg='#4285f4',fg='white',font=('times new roman',12,'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #Botão Apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd= 3, bg='#4285f4',fg='white',font=('times new roman',12,'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #=================================================================

        ##Label entrada Codigo
        self.lb_codigo = Label(self.frame_1, text="Codigo", bg='lightgray',fg='#4285f4')
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.frame_1,bg='white',fg='black',font=('times new roman',12,'bold'))
        self.codigo_entry.place(relx = 0.05, rely = 0.15, relwidth=0.1, relheight =0.1)

        ##Label entrada Nome
        self.lb_nome = Label(self.frame_1, text="Nome" ,bg='lightgray',fg='#4285f4')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1,bg='white',fg='black',font=('times new roman',12,'bold'))
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85, relheight=0.1)

        ##Label entrada Telefone
        self.lb_fone = Label(self.frame_1, text="Telefone", bg='lightgray',fg='#4285f4')
        self.lb_fone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1,bg='white',fg='black',font=('times new roman',12,'bold'))
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.1)

        ##Label entrada cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade",bg='lightgray',fg='#4285f4')
        self.lb_cidade.place(relx=0.50, rely=0.6)

        self.cidade_entry = Entry(self.frame_1,bg='white',fg='black',font=('times new roman',12,'bold'))
        self.cidade_entry.place(relx=0.50, rely=0.7, relwidth=0.4, relheight=0.1)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3,columns=("col1","col2","col3","col4"))
        self.listaCli.heading("#0",text=" ")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0",width= 1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=150)
        self.listaCli.column("#4", width=125)


        self.listaCli.place(relx = 0.01,rely= 0.1, relwidth = 0.95, relheight = 0.85)
        self.scroolLista = Scrollbar(self.frame_2, orient= 'vertical')
        self.listaCli.configure(yscroll = self.scroolLista.set)
        self.scroolLista.place(relx = 0.96 , rely = 0.1,relwidth = 0.04,relheight = 0.85)

        self.listaCli.bind("<Double-1>", self.OnDoubleClick)




Aplication()