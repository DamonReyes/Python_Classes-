import turtle
setup(450, 150, 0, 0)
title("Ejemplo de ventana")
def polygon(t, n, length):
angle= 360/n

for i in range (n):
t.forward(length)
t.left(angle)
t=turtle.Turtle()
polygon(t, 6, 100)