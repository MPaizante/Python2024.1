
 #pip --pre install Pillow 


import turtle

# Set up the turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)  # Set the turtle's speed to draw super fast with no animation

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw a colorful spiral
for _ in range(200):
    t.pencolor(colors[_ % 7])  # Cycle through colors
    t.forward(_)
    t.left(51)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()


