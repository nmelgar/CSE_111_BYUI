# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 800

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    #Top cloud
    x0 = 50
    y0 = 650
    x1 = 150
    y1 = 700

    for i in range(2):
        draw_cloud(canvas, x0, y0, x1, y1)
        y0 += 18
        y1 += 18
        for j in range(2):
            draw_cloud(canvas, x0, y0, x1, y1)
            x0 += 18
            x1 += 18

    #Bottom cloud
    x0 = 600
    y0 = 150
    x1 = 700
    y1 = 200

    for k in range(2):
        draw_cloud(canvas, x0, y0, x1, y1)
        y0 -= 18
        y1 -= 18
        for l in range(2):
            draw_cloud(canvas, x0, y0, x1, y1)
            x0 -= 18
            x1 -= 18

    #Draw moon front
    draw_moon(canvas, 200, 200, 600, 600)
    # draw_cloud(canvas, 250, 300, 300, 350)
    draw_ground(canvas, scene_width, scene_height)
    # Call the finish_drawing function
    # in the draw2d.py library.


# GRID ERASE STARTS HERE------------------------ DELETE LATER
    draw_grid(canvas, scene_width, scene_height, 50)
    finish_drawing(canvas)
# GRID ERASE ENDS HERE-------------------------- DELETE LATER


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 8,
                   scene_width, scene_height, width=0, fill="darkOrchid4")


def draw_cloud(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="darkOrchid2")

def draw_moon(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="darkOrchid3")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height / 8, width=0, fill="gray1")

# GRID ERASE STARTS HERE------------ ----------------DELETE LATER


def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# GRID ERASE ENDS HERE-------------------------------- DELETE LATER


# Call the main function so that
# this program will start executing.
main()
