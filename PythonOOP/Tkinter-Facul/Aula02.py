from tkinter import  *
from  tkinter import ttk

root = Tk()

v = ttk.Scrollbar(root, orient = VERTICAL)
h = ttk.Scrollbar(root, orient= HORIZONTAL)

canvas = Canvas(root, scrollregion=(0,0,1000,1000), yscrollcommand= v.set, xscrollcommand= h.set )
h['command'] = canvas.xview
v['command'] = canvas.yview

ttk.Sizegrip(root).grid(column = 1 , row = 1 , sticky = (S,E))

canvas.grid(column = 0 , row = 0, sticky = (N,W,E,S))
h.grid(column = 0 , row = 1, sticky = (W,E))
v.grid(column = 1 , row = 1, sticky = (N,S))
root.grid_columnconfigure(0, weight= 1)
root.grid_rowconfigure(0, weight= 1)

lastx , lasty = 0 , 0
def xy(event):
    global  lastx , lasty
    lastx , lasty = canvas.canvasx(event.x) , canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', "paletteSelected")
    canvas.itemconfigure('palette', outlline = "white")
    canvas.addtag('paletteSelected' , 'withtag',"palette%s"%color)
    canvas.itemconfigure("paletteSelected", outline = "#999999")
def addLine(event):
    global lastx,lasty
    x , y = canvas.canvasx(event.x) , canvas.canvasy(event.y)
    canvas.create_line((lastx,lasty,x,y), fill=color , width= 5, tags="currentline")
    lastx, lasty = x, y
def doneStroke(event):
    canvas.itemconfigure("currentline", width = 1)

canvas.bind("<Button-1>",xy)
canvas.bind("<B1-Motion>",addLine)

root.mainloop()