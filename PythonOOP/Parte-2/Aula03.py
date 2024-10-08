from tkinter import *
import os

c = os.path.dirname(__file__)
nomeArquivo = c + "\\nomes.txt"

def impDados():
    arquivo = open(nomeArquivo,'a')
    arquivo.write(f"\nNome: {vnome.get()}")
    arquivo.write(f"\nTelefone: {vfone.get()}")
    arquivo.write(f"\nEmail: {vemail.get()}")
    arquivo.write(f"\nTexto: {vtxt.get("1.0",END)}")
    arquivo.write("\n\n")
    arquivo.close()

app= Tk()
app.title("CFB Cursos")
app.geometry("800x800")
app.configure(background="gray")

Label(app,text="Nome",background="#fff",foreground="blue",anchor=W).place(x = 10, y = 5, width =100, height = 20)
vnome = Entry(app)
vnome.place(x = 10 , y =30 , width = 200, height = 20)


Label(app,text="Telefone",background="#fff",foreground="blue",anchor=W).place(x = 10, y = 65, width =100, height = 20)
vfone = Entry(app)
vfone.place(x = 10 , y =90 , width = 120, height = 20)

Label(app,text="Email",background="#fff",foreground="blue",anchor=W).place(x = 10, y = 150, width =100, height = 20)
vemail = Entry(app)
vemail.place(x = 10 , y =190 , width = 130, height = 20)

Label(app,text="OBS",background="#fff",foreground="blue",anchor=W).place(x = 10, y = 300, width =120, height = 20)
vtxt = Text(app)
vtxt.place(x = 10 , y =350 , width = 400, height = 80)

bnt = Button(app,text="Gravar Dados",command=impDados).place(x = 10, y = 500, width =120, height = 20)

app.mainloop()