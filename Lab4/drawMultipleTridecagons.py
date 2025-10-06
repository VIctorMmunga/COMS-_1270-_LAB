#Victor Mmunga
#Date: 9- 24-  2025
#lab: drawMultipleTridecagons #4
# This programm  draw multiples tridecagons by using user input

import turtle
def tridecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(13):
        t.forward(s)
        t.left(360 / 13)
def drawMultipleTridecagons(s, x, y, nr, sr, t):
    for i in range(nr):
        tridecagonTurtle(s, x+i * sr, y, t)
def main():
    s = int(input("Enter side length: "))
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    nr= int(input("Enter number of tridecagons: "))
    sr= int(input("Enter space between tridecagons: "))
    screen= turtle.Screen()
    t= turtle.Turtle()
    drawMultipleTridecagons(s, x, y, nr, sr, t)
    turtle.done()
if __name__ == "__main__":
    main()