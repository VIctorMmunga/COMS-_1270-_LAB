import turtle
def tridecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(13):
        t.forward(s)
        t.left(360 / 13)
def main():
    s = int(input("Enter side length: "))
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    t = turtle.Turtle()
    tridecagonTurtle(s, x, y, t)
    turtle.done()
if __name__ == "__main__":
    main()