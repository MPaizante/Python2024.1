import turtle
import _tkinter
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("Pink")
amy.forward(50)
if amy.pencolor() == "Pink":
    amy.right(60)
    amy.forward(100)
else:
    amy.left(60)
    amy.forward(100)

kenji = turtle.Turtle()
kenji.forward(60)
if kenji.pencolor() == "Pink":
    kenji.right(60)
    kenji.forward(100)
else:
    kenji.left(60)
    kenji.forward(100)
