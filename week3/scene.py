# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)

    diameter = 40
    space = 1
    interval = diameter + space
    top_to_bottom = diameter + space
    x = 150
    y = 120

    for i in range(50):
        draw_oval(canvas, x, y, x + diameter, y + diameter,
              outline="yellow1", fill="yellow1") 
        x += interval
        y += top_to_bottom



    draw_ground(canvas, scene_width, scene_height)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 8,
                   scene_width, scene_height, width=0, fill="darkOrchid4")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height / 8, width=0, fill="gray1")


# Call the main function so that
# this program will start executing.
main()
