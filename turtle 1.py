import turtle
colors = ['red', 'white', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.speed(300)
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.backward(x)
    t.right(59)
    
