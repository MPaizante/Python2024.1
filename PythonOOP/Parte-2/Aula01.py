from tkinter import *
app = Tk()
app.title('Matheus')
app.geometry("500x300")
app.configure(background="blue")

txt = Label(app,text="Matheus",background='black', foreground='white')
txt.place(x = 10, y = 10, width = 70, height = 15)
vtxt = "Modulo Tkinter"
vbg = "pink"
vfg = "gray"
txt2 = Label(app,text=vtxt,background=vbg,foreground=vfg)
#txt2.place(x = 10, y = 30, width = 150, height = 15)
txt2.pack(ipadx = 20, ipady = 20, padx = 5 , side = 'top', fill =X,expand = True)

app.mainloop()