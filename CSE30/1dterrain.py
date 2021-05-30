''' original code is from:
    https://bitesofcode.wordpress.com/2016/12/23/landscape-generation-using-midpoint-displacement/
    and is modified to use turtle graphics
    '''

import random
import bisect
import turtle


# Iterative midpoint vertical displacement
def midpoint_displacement(start, end, roughness, vertical_displacement=None,
                          num_of_iterations=2):
    """
    Given a straight line segment specified by a starting point and an endpoint
    in the form of [starting_point_x, starting_point_y] and [endpoint_x, endpoint_y],
    a roughness value > 0, an initial vertical displacement and a number of
    iterations > 0 applies the  midpoint algorithm to the specified segment and
    returns the obtained list of points in the form
    points = [[x_0, y_0],[x_1, y_1],...,[x_n, y_n]]
    """

    # Final number of points = (2^iterations)+1
    if vertical_displacement is None:
        # if no initial displacement is specified set displacement to:
        #  (y_start+y_end)/2
        vertical_displacement = (start[1] + end[1]) / 2
    # Data structure that stores the points is a list of lists where
    # each sublist represents a point and holds its x and y coordinates:
    # points=[[x_0, y_0],[x_1, y_1],...,[x_n, y_n]]
    #              |          |              |
    #           point 0    point 1        point n
    # The points list is always kept sorted from smallest to biggest x-value
    points = [start, end]
    iteration = 1
    while iteration <= num_of_iterations:
        # Since the list of points will be dynamically updated with the new computed
        # points after each midpoint displacement it is necessary to create a copy
        # of the state at the beginning of the iteration so we can iterate over
        # the original sequence.
        # Tuple type is used for security reasons since they are immutable in Python.
        points_tup = tuple(points)
        for i in range(len(points_tup) - 1):
            # Calculate x and y midpoint coordinates:
            # [(x_i+x_(i+1))/2, (y_i+y_(i+1))/2]
            midpoint = list(map(lambda x: (points_tup[i][x] + points_tup[i + 1][x]) / 2,
                                [0, 1]))
            # Displace midpoint y-coordinate
            midpoint[1] += random.choice([-vertical_displacement,
                                          vertical_displacement])
            # Insert the displaced midpoint in the current list of points         
            bisect.insort(points, midpoint)
            # bisect allows to insert an element in a list so that its order
            # is preserved.
            # By default the maintained order is from smallest to biggest list first
            # element which is what we want.
        # Reduce displacement range
        vertical_displacement *= 2 ** (-roughness)
        # update number of iterations
        iteration += 1
    return points


def draw_layers(layers, width, height, shade=(195, 157, 224)):
    ''' draws one layer at a time instead of a list of layers
    '''

    # convert layers coords to turtle coords
    # turtle origin is at center of screen,
    # whereas calculations assumes origin at lower left
    xoffset = width / 2
    yoffset = height / 2
    for i in range(len(layers)):
        layers[i] = [layers[i][0] - xoffset, layers[i][1] - yoffset]

    global bob  # refer to the global turtle

    bob.penup()
    bob.goto(-xoffset, -yoffset)  # move to bottom left of turtle screen

    turtle.colormode(255)
    bob.fillcolor(shade)
    bob.begin_fill()
    for i in range(len(layers)):
        bob.goto(layers[i])
    bob.goto(width - xoffset, -yoffset)
    bob.goto(-xoffset, -yoffset)
    bob.end_fill()


bob = turtle.Turtle()  # defined as global so that functions can see bob


def main():
    width = 1000  # Terrain width
    height = 500  # Terrain height

    turtle.setup(width, height, startx=None, starty=None)  # set turtle screen size
    turtle.bgcolor("#8899ee")

    bob.speed(0)
    bob.penup()
    bob.goto(-200, 200)
    # bob.pencolor("red")
    bob.fillcolor("yellow")
    bob.begin_fill()
    bob.circle(25)
    bob.end_fill()

    # Compute different layers of the landscape
    layer_1 = midpoint_displacement([250, 0], [width, 200], 1.4, 20, 10)
    layer_2 = midpoint_displacement([0, 180], [width, 80], 1.2, 30, 10)
    layer_3 = midpoint_displacement([0, 270], [width, 190], 1, 120, 9)
    layer_4 = midpoint_displacement([0, 350], [width, 320], 0.9, 250, 8)

    draw_layers(layer_4, width, height, (158, 98, 204))
    draw_layers(layer_3, width, height, (130, 79, 138))
    draw_layers(layer_2, width, height, (68, 28, 99))
    draw_layers(layer_1, width, height, (49, 7, 82))

    bob.goto(400, -220)
    bob.pencolor("yellow")
    bob.write("cse30, spring 2020", align="right", font=("Arial", 10, "normal"))
    bob.goto(600, -300)  # move turtle offscreen

    turtle.done()


if __name__ == "__main__":
    main()