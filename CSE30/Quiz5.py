import turtle


def draw_square(corners, color):
    """ draws a single square and fills with color.
        assumes corners is list of 4 tuples representing the corners. """

    turtle.fillcolor(color)                   # specify fillcolor
    turtle.penup()                              # don't draw anything yet
    turtle.begin_fill()                         # start of shape to fill
    turtle.goto(corners[0][0], corners[0][1])   # starting point of shape
    turtle.pendown()                            # start drawing
    for i in range(len(corners)):               # draw to each corner & back
        turtle.goto(corners[(i+1) % 4][0], corners[(i+1) % 4][1])
    turtle.end_fill()                           # end of shape to fill


colors = [(255, 0, 0),        # red
          (0, 255, 0),        # green
          (0, 0, 255),        # blue
          (128, 128, 128),    # gray
          (132, 31,  1),    # rand1
          (21, 12, 122),    # rand2
          (123, 41, 232),    # rand3
          (32, 121, 49)]    # rand4

pt1 = (-100, 100)
pt2 = (100, 100)
pt3 = (100, -100)
pt4 = (-100, -100)

square = [pt1, pt2, pt3, pt4]    # outermost square

sq2pt1 = (-100, 70)
sq2pt2 = (70, 100)
sq2pt3 = (100, -70)
sq2pt4 = (-70, -100)

square2 = [sq2pt1, sq2pt2, sq2pt3, sq2pt4]

sq3pt1 = (-95, 45)
sq3pt2 = (45, 95)
sq3pt3 = (95, -45)
sq3pt4 = (-45, -95)

square3 = [sq3pt1, sq3pt2, sq3pt3, sq3pt4]

sq4pt1 = (-85, 18)
sq4pt2 = (18, 85)
sq4pt3 = (85, -18)
sq4pt4 = (-18, -85)

square4 = [sq4pt1, sq4pt2, sq4pt3, sq4pt4]

sq5pt1 = (-70, -5)
sq5pt2 = (-5, 70)
sq5pt3 = (70, 5)
sq5pt4 = (5, -70)

square5 = [sq5pt1, sq5pt2, sq5pt3, sq5pt4]

sq6pt1 = (-55, -18)
sq6pt2 = (-18, 55)
sq6pt3 = (55, 18)
sq6pt4 = (18, -55)

square6 = [sq6pt1, sq6pt2, sq6pt3, sq6pt4]

sq7pt1 = (-40, -25)
sq7pt2 = (-25, 40)
sq7pt3 = (40, 25)
sq7pt4 = (25, -40)

square7 = [sq7pt1, sq7pt2, sq7pt3, sq7pt4]

sq8pt1 = (-25, -28)
sq8pt2 = (-28, 25)
sq8pt3 = (25, 28)
sq8pt4 = (28, -25)

square8 = [sq8pt1, sq8pt2, sq8pt3, sq8pt4]

turtle.setup()              # setup canvas using default params
turtle.colormode(255)       # colors are defined as triples of 0..255 each
turtle.speed(0)             # draw as fast as you can
bob = turtle.Turtle()       # create drawing turtle

draw_square(square, colors[0])
draw_square(square2, colors[1])
draw_square(square3, colors[2])
draw_square(square4, colors[3])
draw_square(square5, colors[4])
draw_square(square6, colors[5])
draw_square(square7, colors[6])
draw_square(square8, colors[7])

ts = turtle.getscreen()
turtle.done()
