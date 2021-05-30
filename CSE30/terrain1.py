# COPY THIS CODE TO CREATE A .py FILE TO RUN or COPY TO A JUPYTER (NOT COLAB) NOTEBOOK AND RUN
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:04:11 2020
CSE 30 Spring 2020 Program 1 helper code
@author: Fahim
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
VERTICES = [(-1, -0.75, 0), (1.25, -0.5, 0), (0, 1.5, 0)]
TRIANGLES = [(0, 1, 2)]
recurred_midpoints = []


def midpoint_displacement(x1, y1, z1, x2, y2, z2, x3, y3, z3, level):
    if level <= 0:
        recurred_midpoints.append((x1, y1, z1))
        recurred_midpoints.append((x2, y2, z2))
        recurred_midpoints.append((x3, y3, z3))
        # return recurred_midpoints
    else:
        mx1 = (x1 + x2) / 2
        my1 = (y1 + y2) / 2
        mz1 = ((z1 + z2) / 2) + (random.uniform(0.0, 0.2) * (level))
        mx2 = (x2 + x3) / 2
        my2 = (y2 + y3) / 2
        mz2 = ((z2 + z3) / 2) + (random.uniform(0.0, 0.2) * (level))
        mx3 = (x3 + x1) / 2
        my3 = (y3 + y1) / 2
        mz3 = ((z1 + z2) / 2) + (random.uniform(0.0, 0.2) * (level))

        midpoint_displacement(mx3, my3, mz3, mx2, my2, mz2, mx1, my1, mz1, level - 1)
        midpoint_displacement(x1, y1, z1, mx1, my1, mz1, mx3, my3, mz3, level - 1)
        midpoint_displacement(mx3, my3, mz3, mx2, my2, mz2, x3, y3, z3, level - 1)
        midpoint_displacement(mx1, my1, mz1, x2, y2, z2, mx2, my2, mz2, level - 1)


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

    # Turn off move time for instant drawing
    turtle.tracer(0, 0)
    terrain.up()
    angle = 0

    for point in TRIANGLES:
        verts = [VERTICES[point[0]], VERTICES[point[1]], VERTICES[point[2]]]

        midpoint_displacement(verts[0][0], verts[0][1], verts[0][2], verts[1][0], verts[1][1], verts[1][2],
                              verts[2][0], verts[2][1], verts[2][2], 3)

    while True:
        # Clear the screen
        terrain.clear()

        # Transform the terrain
        VERT2D = []
        for vert3D in recurred_midpoints:
            x, y, z = vert3D
            sx, sy = transform(x, y, z, angle, 1.5708)
            VERT2D.append((sx, sy))

        # This code moves a single triangle at point z
        """for index in range(0, len(recurred_midpoints), 3):
            points = [(VERT2D[index], VERT2D[index + 1], VERT2D[index + 2])]
        """

        points = [VERT2D[j:j + 3] for j in range(0, len(VERT2D), 3)]

        # Draw the triangles
        for i in points:
            terrain.goto(i[0][0], i[0][1])
            terrain.down()

            terrain.goto(i[1][0], i[1][1])
            terrain.goto(i[2][0], i[2][1])
            terrain.goto(i[0][0], i[0][1])

            terrain.up()

        # Update screen
        turtle.update()

        # Control the speed of animation
        angle += 0.0005


if __name__ == "__main__":
    main()
