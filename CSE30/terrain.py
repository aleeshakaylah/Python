# COPY THIS CODE TO CREATE A .py FILE TO RUN or COPY TO A JUPYTER (NOT COLAB) NOTEBOOK AND RUN
# -*- coding: utf-8 -*-

"""
CSE 30 Spring 2020 Program 1 
"""

import math
import random
import turtle

# Note: For this example, we are using hardcoded points/vertices to test the functionalities of the viewer and
# animation. For Program 1, you need to replace the code between the tags # BEGIN and # END with your code. Your code
# should generate the VERTICES and TRIANGLES using your recursive "midpoint_displacement" function. This setup is
# optimized for points values generated in the range -1.00 to 1.00. You may need the adjust the value of FOV to
# generate points with higher ranges.


# BEGIN
# =====================================================================
# Level 0 terrain (1 triangle)
VERTICES = []
TRIANGLES = []


def midpoint_displacement(x1, y1, z1, x2, y2, z2, x3, y3, z3, displace, roughness, level):
    if level == 1:
        VERTICES.append((x1, y1, z1))
        VERTICES.append((x2, y2, z2))
        VERTICES.append((x3, y3, z3))
        TRIANGLES.append((len(VERTICES) - 3, len(VERTICES) - 2, len(VERTICES) - 1))
        # print(VERTICES)
        # print(TRIANGLES)

        # return VERTICES, TRIANGLES
    else:
        displace = displace * roughness
        mx1 = (x1 + x2) / 2
        my1 = (y1 + y2) / 2
        mz1 = (z1 + z2) / 2 + displace

        mx2 = (x2 + x3) / 2
        my2 = (y2 + y3) / 2
        mz2 = (z2 + z3) / 2 + displace

        mx3 = (x3 + x1) / 2
        my3 = (y3 + y1) / 2
        mz3 = (z1 + z2) / 2 + displace

        displace = displace / level * roughness
        midpoint_displacement(mx3, my3, mz3, mx2, my2, mz2, mx1, my1, mz1, displace, roughness, level - 1)
        midpoint_displacement(x1, y1, z1, mx1, my1, mz1, mx3, my3, mz3, displace, roughness, level - 1)
        midpoint_displacement(mx1, my1, mz1, x2, y2, z2, mx2, my2, mz2, displace, roughness, level - 1)
        midpoint_displacement(mx3, my3, mz3, mx2, my2, mz2, x3, y3, z3, displace, roughness, level - 1)


# =====================================================================
# END

def transform(x, y, z, angle, tilt):
    # Animation control (around y-axis). For a view of earth from space, it's moving over the equator.
    s, c = math.sin(angle), math.cos(angle)
    x, y = x * c - y * s, x * s + y * c

    # Camera tilt  (around x-axis). For a view of earth from space, the tilt angle is measure from the equator.
    s, c = math.sin(tilt), math.cos(tilt)
    z, y = z * c - y * s, z * s + y * c

    # Setting up View Parameters
    y += 5  # Fixed Distance from top
    FOV = 1000  # Fixed Field of view
    f = FOV / y
    sx, sy = x * f, z * f
    return sx, sy


def main():
    terrain = turtle.Turtle()
    terrain.pencolor("blue")
    terrain.pensize(2)

    height = 1000
    width = 1000
    turtle.screensize(height, width)

    # Turn off move time for instant drawing
    turtle.tracer(0, 0)
    terrain.up()
    angle = 0
    # print(VERTICES)

    VERTEX = []
    TRIANGLE = []

    VERTEX.append((-1, -0.75, 0))
    VERTEX.append((1.25, -0.5, 0))
    VERTEX.append((0, 1.5, 0))

    '''
    VERTEX.append((0, 0.5, 0))
    VERTEX.append((1, 1, 1))
    VERTEX.append((0.75, 0, 0))
    '''

    # VERTICES = [(0, 20, 0), (20, 0, 0), (-20, 0, 0)]
    TRIANGLE.append((0, 1, 2))

    x1 = VERTEX[TRIANGLE[0][0]][0]
    y1 = VERTEX[TRIANGLE[0][0]][1]
    z1 = VERTEX[TRIANGLE[0][0]][2]

    x2 = VERTEX[TRIANGLE[0][1]][0]
    y2 = VERTEX[TRIANGLE[0][1]][1]
    z2 = VERTEX[TRIANGLE[0][1]][2]

    x3 = VERTEX[TRIANGLE[0][2]][0]
    y3 = VERTEX[TRIANGLE[0][2]][1]
    z3 = VERTEX[TRIANGLE[0][2]][2]

    # print(VERTICES)
    # print(TRIANGLES)
    displacement = random.uniform(0.0, 0.5)

    midpoint_displacement(x1, y1, z1, x2, y2, z2, x3, y3, z3, displacement, 1.5, 5)

    while True:
        # Clear the screen
        terrain.clear()

        # Transform the terrain
        VERT2D = []
        for vert3D in VERTICES:
            x, y, z = vert3D
            sx, sy = transform(x, y, z, angle, 1.5708)
            VERT2D.append((sx, sy))

        # Draw the terrain
        for triangle in TRIANGLES:
            points = [VERT2D[triangle[0]], VERT2D[triangle[1]], VERT2D[triangle[2]]]

            # Draw the square
            terrain.goto(points[0][0], points[0][1])
            terrain.down()

            terrain.goto(points[1][0], points[1][1])
            terrain.goto(points[2][0], points[2][1])
            terrain.goto(points[0][0], points[0][1])

            terrain.up()

        # Update screen
        turtle.update()

        # Control the speed of animation
        angle += 0.005


if __name__ == "__main__":
    main()
