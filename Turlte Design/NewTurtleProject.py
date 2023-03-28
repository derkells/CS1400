# Begin by copying your code from Turtle Patterns I and pasting it here.
# Alternatively, you may download your code from Turtle Patterns I and
# upload it here.
'''
Project Name: Turtle Patterns 2
Author: Derek Ellsworth
Due Date: 2023/02/03
Course: CS1400-001



This is a project that utilizes functions, for loops, and a library to draw a scene of trees and a house.
To run the program type run_doodles.py normal -s (you can substitute normal with the word wacky or boring).
The code runs a Turtle window that is 500x500 and draws a smaller copy of the scene directly
within the normal sized version of the scene.
'''
import turtle
import math


def draw(option):
    '''This is the main function for the program that houses the rest'''
    width = 500
    height = 500
    # Initialization
    screensize = turtle.getscreen()
    screensize.setup(width=width, height=height, startx=0, starty=0)
    pen = turtle.Turtle()

    if option[0] == 'normal':
        draw_sun('yellow', -95, 80, 70)
        draw_normal_scene(0, 400, 'cornsilk4', pen)
        pen.right(90)
        # draw_normal_scene(0,50,'green', pen)
        draw_trees(0, 70, 'Green', width, height+50)
    elif option[0] == 'wacky':
        draw_sun('blue', -95, 80, 70)
        draw_wacky_scene(0, 400, 'blue', pen)
        pen.right(90)
        draw_trees(0, 70, 'slateblue4', width, height+50)
    elif option[0] == 'boring':
        draw_sun('peru', -95, 80, 70)
        draw_boring_scene(0, 400, 'blue', pen)
        pen.right(90)
        draw_trees(0, 70, 'orange4', width, height+50)
    else:
        print('Invalid option, check spelling. choose between normal, wacky, and boring')


def draw_normal_scene(tilt, size, color, pen):
    '''This function draws the normal scene'''
    draw_house_rectangle(tilt, size, 'cornsilk4', pen)
    draw_roof_triangle(tilt, size, 'DarkOrange4', pen)
    draw_window(-size/4, -size/4, size/4, 'CadetBlue1', pen)
    draw_window(size/4, -size/4, size/4, 'CadetBlue1', pen)
    pen.penup()
    pen.goto(0, 0)
    pen.goto(0, size/12)
    pen.pendown()
    draw_normal_centered_rectangle(tilt, size, 'white', pen)


def draw_wacky_scene(tilt, size, color, pen):
    '''This function draws the wacky scene'''
    draw_house_rectangle(tilt, size, 'hotpink3', pen)
    draw_roof_triangle(tilt, size, 'LightSeaGreen', pen)
    draw_window(-size/4, -size/4, size/4, 'yellow3', pen)
    draw_window(size/4, -size/4, size/4, 'salmon1', pen)
    pen.penup()
    pen.goto(0, 0)
    pen.goto(0, size/12)
    pen.pendown()
    draw_wacky_centered_rectangle(tilt, size, 'white', pen)


def draw_boring_scene(tilt, size, color, pen):
    '''This function draws the boring scene'''
    draw_house_rectangle(tilt, size, 'cornsilk', pen)
    draw_roof_triangle(tilt, size, 'cornsilk3', pen)
    draw_window(-size/4, -size/4, size/4, 'moccasin', pen)
    draw_window(size/4, -size/4, size/4, 'moccasin', pen)
    pen.penup()
    pen.goto(0, 0)
    pen.goto(0, size/12)
    pen.pendown()
    draw_boring_centered_rectangle(tilt, size, 'white', pen)


def draw_wacky_centered_rectangle(tilt, size, color, pen):
    '''This function draws the small wacky scene in a box'''
    pen.right(180)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size/8)
        pen.left(90)
        pen.forward(size/4)
        pen.left(90)
        pen.forward(size/8)
    pen.end_fill()
    draw_sun('blue', -16, 82, 8)
    draw_small_wacky_scene(0, 50, 'green', pen)
    draw_small_tree(tilt, 9, color, -48, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, -37, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, -26, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, -15, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, -4, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, 7, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, 18, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, 29, 48, 'slateblue4')
    draw_small_tree(tilt, 9, color, 40, 48, 'slateblue4')


def draw_boring_centered_rectangle(tilt, size, color, pen):
    '''This function draws the small boring scene in a box'''
    pen.right(180)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size/8)
        pen.left(90)
        pen.forward(size/4)
        pen.left(90)
        pen.forward(size/8)
    pen.end_fill()
    draw_sun('peru', -16, 82, 8)
    draw_small_boring_scene(0, 50, 'green', pen)
    draw_small_tree(tilt, 9, color, -48, 48, 'orange4')
    draw_small_tree(tilt, 9, color, -37, 48, 'orange4')
    draw_small_tree(tilt, 9, color, -26, 48, 'orange4')
    draw_small_tree(tilt, 9, color, -15, 48, 'orange4')
    draw_small_tree(tilt, 9, color, -4, 48, 'orange4')
    draw_small_tree(tilt, 9, color, 7, 48, 'orange4')
    draw_small_tree(tilt, 9, color, 18, 48, 'orange4')
    draw_small_tree(tilt, 9, color, 29, 48, 'orange4')
    draw_small_tree(tilt, 9, color, 40, 48, 'orange4')


def draw_small_scene(tilt, size, color, pen):
    '''This function draws the small normal scene in a box'''
    draw_small_house_rectangle(tilt, size, 'cornsilk4', pen)
    draw_small_roof_triangle(tilt, size, 'DarkOrange4', pen)
    draw_small_window(-12, 62, size/4, 'CadetBlue1', pen)
    draw_small_window(12, 62, size/4, 'CadetBlue1', pen)
    pen.penup()
    pen.goto(0, 0)
    pen.goto(0, size/12)
    pen.pendown()


def draw_small_wacky_scene(tilt, size, color, pen):
    '''Draws the small wacky scene'''
    draw_small_house_rectangle(tilt, size, 'hotpink3', pen)
    draw_small_roof_triangle(tilt, size, 'LightSeaGreen', pen)
    draw_small_window(-12, 62, size/4, 'yellow3', pen)
    draw_small_window(12, 62, size/4, 'salmon1', pen)
    pen.penup()
    pen.goto(0, 0)
    pen.goto(0, size/12)
    pen.pendown()


def draw_small_boring_scene(tilt, size, color, pen):
    '''draws the small boring scene'''
    draw_small_house_rectangle(tilt, size, 'cornsilk', pen)
    draw_small_roof_triangle(tilt, size, 'cornsilk3', pen)
    draw_small_window(-12, 62, size/4, 'moccasin', pen)
    draw_small_window(12, 62, size/4, 'moccasin', pen)
    pen.penup()
    pen.goto(0, 0)
    pen.goto(0, size/12)
    pen.pendown()


def draw_small_window(x_axis, y_axis, size, color, pen):
    '''Used to draw small windows'''
    window_width = size/2
    window_height = size/2
    pen.penup()
    pen.goto(x_axis, y_axis)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(window_width)
        pen.left(90)
        pen.forward(window_height)
        pen.left(90)
    pen.end_fill()


def draw_small_house_rectangle(tilt, size, color, pen):
    '''Used to draw small house body'''
    pen.penup()
    pen.goto(-25, 50)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size)
        pen.left(90)
        pen.forward(size/2)
        pen.left(90)
    pen.end_fill()


def draw_small_roof_triangle(tilt, size, color, pen):
    '''used to draw small house roof'''
    pen.penup()
    pen.goto(-25, 75)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(45)
    pen.forward(math.sqrt(2)*size/2)
    pen.right(90)
    pen.forward(math.sqrt(2)*size/2)
    pen.right(135)
    pen.forward(size)
    pen.end_fill()


def draw_small_tree(tilt, size, color, starting_position, ground, new_color):
    '''draws individual small tree'''
    # initialization of the new turtle and positioning, The new turtle and positioning are required to put the atomic shape functions in the right position
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(starting_position+2, ground+8)
    pen.pendown()
    draw_rectangle(0, size, 'Brown', pen)
    ending_trunk_position = pen.position()
    pen.penup()
    pen.goto(ending_trunk_position[0]-5, ending_trunk_position[1])
    draw_triangle(0, size+5, new_color, pen)
    pen.hideturtle()


def draw_normal_centered_rectangle(tilt, size, color, pen):
    '''Draws the box for small scene'''
    pen.right(180)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size/8)
        pen.left(90)
        pen.forward(size/4)
        pen.left(90)
        pen.forward(size/8)
    pen.end_fill()
    draw_sun('yellow', -16, 82, 8)
    draw_small_scene(0, 50, 'green', pen)
    draw_small_tree(tilt, 9, color, -48, 48, 'green')
    draw_small_tree(tilt, 9, color, -37, 48, 'green')
    draw_small_tree(tilt, 9, color, -26, 48, 'green')
    draw_small_tree(tilt, 9, color, -15, 48, 'green')
    draw_small_tree(tilt, 9, color, -4, 48, 'green')
    draw_small_tree(tilt, 9, color, 7, 48, 'green')
    draw_small_tree(tilt, 9, color, 18, 48, 'green')
    draw_small_tree(tilt, 9, color, 29, 48, 'green')
    draw_small_tree(tilt, 9, color, 40, 48, 'green')
    # pen.goto(0,size/4)
    # pen.pendown()


# Draws a little rectangle on the house
def draw_window(x_axis, y_axis, size, color, pen):
    '''Draws a window'''
    window_width = size/2
    window_height = size/2
    pen.penup()
    pen.goto(x_axis, y_axis)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(window_width)
        pen.left(90)
        pen.forward(window_height)
        pen.left(90)
    pen.end_fill()

# Draws a Rectangle for the house


def draw_house_rectangle(tilt, size, color, pen):
    '''Draws house body'''
    pen.penup()
    pen.goto(-size/2, -size/2)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size)
        pen.left(90)
        pen.forward(size/2)
        pen.left(90)
    pen.end_fill()

# Draws an isosolese triangle for the roof


def draw_roof_triangle(tilt, size, color, pen):
    '''Draws house roof'''
    pen.penup()
    pen.goto(-size/2, 0)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(45)
    pen.forward(math.sqrt(2)*size/2)
    pen.right(90)
    pen.forward(math.sqrt(2)*size/2)
    pen.right(135)
    pen.forward(size)
    pen.end_fill()


# Draws a Circle
def draw_sun(color, x_axis, y_axis, size):
    '''used to draw the sun'''
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(x_axis, y_axis)
    pen.fillcolor(color)
    # pen.right(tilt) #Circle tilting
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    pen.hideturtle()


def draw_trees(tilt, size, color, starting_position, ground):
    '''Used to draw the trees'''
    # initialization of the new turtle and positioning, The new turtle and positioning are required to put the atomic shape functions in the right position
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(-(starting_position/2), -(ground*.25))
    starting_point = pen.position()
    pen.pendown()

    tracker = 0
    for _ in range(0, starting_position, 75):
        pen.goto(starting_point[0] + tracker, -(ground*.25))
        tracker += 75
    # Creates the Tree Trunk
        draw_rectangle(0, size, 'Brown', pen)
        ending_trunk_position = pen.position()

    # Creates the crown of the tree with the specified color
        pen.penup()
        pen.goto(ending_trunk_position[0]-size/3.5, -(ground*.25))
        draw_triangle(0, size+5, color, pen)


def draw_rectangle(tilt, size, color, pen):
    '''Used to draw normal rectangle'''
    pen.right(tilt)  # Tilting the rectangle
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size/2)
        pen.right(90)
        pen.forward(size)
        pen.right(90)
    pen.end_fill()


def draw_square(tilt, size, color, pen):
    '''Used to draw normal square'''
    pen.fillcolor(color)
    pen.begin_fill()  # Tilting the square
    pen.right(tilt)
    for _ in range(4):  # Makes the base of the house
        pen.forward(size)
        pen.right(90)
    pen.end_fill()


def draw_triangle(tilt, size, color, pen):
    '''Used to draw triangle'''
    pen.fillcolor(color)
    pen.begin_fill()
    pen.right(tilt)  # tilting the triangle

    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()
