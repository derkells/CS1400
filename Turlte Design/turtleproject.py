'''
Project Name: Turtle PAtterns I
Author: Derek Ellsworth
Due Date: 2023/02/03
Course: CS1400-001



This is a project that utilizes functions, for loops, and a library to draw a scene of trees and a house.
You will enter 2 different values, the first for width, the second for height, the ideal height and width are 500
You can go into the "draw" function if you wish to change color and tilt of the shapes on the canvas.
For work I use Javascript so a lot of this was learning the correct syntax and reading the turtle documentation.
'''
# (3) add functions here that your main program calls
# to do stuff.
import turtle


#Fancy Amazing Artwork Functions that utilize my Atomic Shape Functions
def draw_house(tilt, size, color, pen):
    draw_square(0,size,color, pen) #Walls of House
    draw_triangle(0,size,color, pen) #Roof of house

def draw_sun(tilt, size, color, position): #Seems redundant but this is the portion of the drawing that "Draw" is calling, it is using my draw_circle function 
    draw_circle(0,size,color, position)

def draw_trees(tilt, size, color, starting_position, ground):
    #initialization of the new turtle and positioning, The new turtle and positioning are required to put the atomic shape functions in the right position
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(-(starting_position/2), -(ground*.25))
    starting_point = pen.position()
    pen.pendown()

    tracker = 0
    for _ in range(0, starting_position, 75):
        pen.goto( starting_point[0]+ tracker, -(ground*.25))
        tracker += 75
    #Creates the Tree Trunk
        draw_rectangle(0,size,'Brown',pen)
        ending_trunk_position = pen.position()

    #Creates the crown of the tree with the specified color
        pen.penup()
        pen.goto(ending_trunk_position[0]-size/3.5,-(ground*.25))
        draw_triangle(0, size+5, color, pen)




#Atomic Shap Functions
def draw_circle(tilt,size,color,position):
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(0,position/4)
    pen.fillcolor(color)
    pen.right(tilt) #Circle tilting
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

def draw_rectangle(tilt,size,color,pen):
    pen.right(tilt) #Tilting the rectangle
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size/2)
        pen.right(90)
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

def draw_square(tilt, size, color, pen):
    pen.fillcolor(color)
    pen.begin_fill() #Tilting the square
    pen.right(tilt)
    for _ in range(4): #Makes the base of the house
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

def draw_triangle(tilt, size, color, pen):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.right(tilt) #tilting the triangle

    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def get_dimensions():
    width = int(input()) #Use 500 for testing
    height = int(input()) #Use 500 for testing

    if (width > 0 and height > 0):
        return width, height
    else: 
        raise ValueError('Width and height must be positive integers.')

    

def draw(width, height):
    '''
    Sets the size of the screen to width and height and draws a doodle.
    '''
    #Initialization
    screensize = turtle.getscreen()
    screensize.setup (width=width, height=height, startx=0, starty=0)
    pen = turtle.Turtle()

    draw_sun(0,50,'Yellow', height)
    draw_house(0,100,'Blue', pen)
    draw_trees(0,60,'Green', width, height)


    #Comment out the above 3 function calls and uncomment these
    #if you want to mess around with individual Atomic Shape functions

    draw_circle(0,0,'Orange',height) 
    draw_rectangle(0,0,'black',pen)
    draw_square(0,0, 'Blue', pen)
    draw_triangle(0,0,'Purple', pen)

draw(500,500)