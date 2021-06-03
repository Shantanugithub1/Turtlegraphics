import turtle
colors = ["red","blue","green","yellow","pink","orange"]
hexagon = turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
    hexagon.pencolor(colors[i%6])
    hexagon.width(i/100+1)
    hexagon.forward(i)
    hexagon.left(59)