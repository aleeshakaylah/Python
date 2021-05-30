import turtle


def drawC(x1, y1, x2, y2, color, level):
    turtle.pencolor(color)
    if level == 0:
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
    else:
        mx = (x1 + x2 + y1 - y2) / 2
        my = (x2 + y1 + y2 - x1) / 2
        drawC(x1, y1, mx, my, color, level - 1)
        drawC(mx, my, x2, y2, color, level - 1)


turtle.setup()
turtle.bgcolor("#aa9922")
turtle.speed(8)
turtle.colormode(255)
turtle.width(4)

color = (12, 50, 231)

# drawC(0,-100, 0, 100, color, 12)
drawC(-100, -100, 0, 100, color, 6)

turtle.done()
