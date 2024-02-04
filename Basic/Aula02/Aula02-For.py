print("This will execute first")
print("-"*60)

for x in range(3):
    print("This line will execute three times") 
    print("This line will also execute three times")
    print("-"*60)
    
print("Final")

import turtle
wn = turtle.Screen()
elan = turtle.Turtle()
distance = 50
angle = 90
for x in range(10):
    elan.forward(distance)
    elan.right(90)
    distance +=10
    angle = angle - 3