"""
CSAP/X Mondrian recursion lab
Author: RIT CS
Author: Mia McSwain

Student starter code for the mondrian square lab.  It prompts for a depth of
recursion (between 1-8) and random subdivisions, and recursively generates
colored rectangles.
"""

import turtle
import random

# depth range for input
MIN_DEPTH=1
MAX_DEPTH=8

# the four colors of rectangles
COLORS = ['blue', 'red', 'white', 'yellow']

# screen dimensions and inlay offset for image
WIDTH = 800
HEIGHT = 800
INLAY = 20

def init(depth: int, rand: bool) -> None:
    """
    Set up the display.  This is called by:
        main
    :param depth: user's desired depth
    :param rand: random subdivisions or not
    """
    # use speed(0) when developing so you can see the animations
    #turtle.speed(0)
    turtle.tracer(0) #when finished developing turn animations of for fastest rendering
    # set screen dimensions
    turtle.Screen().setup(WIDTH, HEIGHT)
    # world coordinates are llx -20, lly -20, urx 820, ury 820
    turtle.setworldcoordinates(-INLAY, -INLAY, WIDTH+INLAY, HEIGHT+INLAY)
    # image will render in llx 0, lly 0, urx 800, ury 800
    turtle.setpos(0,0)
    # black pen outline size is 1
    turtle.pensize(1)
    # title includes key values
    turtle.title(f'Mondrian, depth={depth}, random={rand}, width={WIDTH}, height={HEIGHT}')
    # don't ever show turtle on screen - can be turned off when developing
    turtle.hideturtle()

def draw_rectangle(area_list : list, llx : int, lly : int, urx : int, ury : int):
    """
    Draws a rectangle using the parameter's as coordinates, fills it with a random color,
    computes the area of the rectangle, and edits the appropriate array value
    :param area_list: List with indexes for the blue area, red area, white area, and yellow area
    :param llx: Lower left x coordinate
    :param lly: Lower left y coordinate
    :param urx: Upper right x coordinate
    :param ury: Upper right y coordinate
    :return: Returns a list containing the current surface area for each color
    """
    x_len = urx-llx
    y_len = ury-lly
    color = random.choice(COLORS)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(x_len)
        turtle.left(90)
        turtle.forward(y_len)
        turtle.left(90)
    turtle.end_fill()
    if color == 'blue':
        area_list[0] += x_len * y_len
    elif color == 'red':
        area_list[1] += x_len * y_len
    elif color == 'white':
        area_list[2] += x_len * y_len
    else:
        area_list[3] += x_len * y_len
    return area_list

def move_to(x : int, y : int) -> None:
    """
    Teleports turtle to specified location without drawing
    :param x: X coordinate of new location
    :param y: Y coordinate of new location
    :return:
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def draw_rectangle_rec(sur_area_list :list, depth :int, rand_sub : str, llx : int, lly : int, urx : int, ury : int):
    """
    Recursively draws a grid of either evenly-sized rectangles or randomly sized rectangles
    :param sur_area_list: List with indexes for the blue area, red area, white area, and yellow area
    :param depth: The amount of times the function will recurse
    :param rand_sub: Whether the subdivisions will be random dimensions or not
    :param llx: Lower left x coordinate
    :param lly: Lower left y coordinate
    :param urx: Upper right x coordinate
    :param ury: Upper right y coordinate
    :return: Returns a list containing the surface area for each color
    """
    if depth == 1:
        sur_area_list = draw_rectangle(sur_area_list, llx, lly, urx, ury)
    else:
        if rand_sub == 'y':
            cx = random.randint(llx, urx)
            cy = random.randint(lly, ury)
        else:
            cx = (llx + urx) // 2
            cy = (lly + ury) // 2

        move_to(llx, lly)
        draw_rectangle_rec(sur_area_list, depth - 1, rand_sub, llx, lly, cx, cy)
        move_to(cx, lly)
        draw_rectangle_rec(sur_area_list, depth - 1, rand_sub, cx, lly, urx, cy)
        move_to(cx, cy)
        draw_rectangle_rec(sur_area_list, depth - 1, rand_sub, cx, cy, urx, ury)
        move_to(llx, cy)
        draw_rectangle_rec(sur_area_list, depth - 1, rand_sub, llx, cy, cx, ury)
        move_to(llx, lly)
    return sur_area_list


def main() -> None:
    """
    The main method.
    """
    # prompt for depth
    depth = int(input("Enter depth? "))
    while depth < MIN_DEPTH or depth > MAX_DEPTH:
        depth = int(input("Enter depth? "))

    # prompt for choice of random subdivisions
    random_sub = str(input("Random subdivisions? "))

    # initialize display
    init(0, False)

    # initialize surface area list
    surface_area = [0, 0, 0, 0]

    # draw the image
    rec = draw_rectangle_rec(surface_area, depth, random_sub, 0, 0, WIDTH, HEIGHT)

    # print surface area
    print("Rectangle Surface Areas:\n\t blue: {}\n\t red: {}\n\t white: {}\n\t yellow: {}"
          .format(rec[0], rec[1], rec[2], rec[3]))
    print("Total Surface Area: {}".format(rec[0] + rec[1] + rec[2] + rec[3]))

    # if the tracer is turned off, update the final drawing
    turtle.update()

    # wait for user to exit
    turtle.mainloop()

if __name__ == '__main__':
    main()
