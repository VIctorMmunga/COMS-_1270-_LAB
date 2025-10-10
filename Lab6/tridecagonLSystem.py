
# Name: Victor Mmunga
# Date: 10 -06- 2025
# Lab: tridecagonLSystem
# Description: L-system modified to include:
# "T" draws a tridecagon, "P" moves turtle to a random location.

import turtle
import random
from tridecagonTurtle import tridecagonTurtle
def applyRules(ch):
    if ch == 'F':
        return 'F-T+PF'  
    else:
        return ch
def processString(oldStr):
    newStr = ""
    for ch in oldStr:
        newStr += applyRules(ch)
    return newStr
def createLSystem(numIters, axiom):
    startString = axiom
    for _ in range(numIters):
        startString = processString(startString)
    return startString
def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'T':
            tridecagonTurtle(distance, aTurtle.xcor(), aTurtle.ycor(),aTurtle)
        elif cmd == 'P':
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            aTurtle.penup()
            aTurtle.goto(x, y)
            aTurtle.pendown()
def main():
    axiom = "F"
    iterations = 3
    instructions = createLSystem(iterations, axiom)
    print("L-System instructions:", instructions)
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.speed(0)  
    wn= turtle.Screen()
    drawLsystem(t, instructions, 60, 20)
    wn.exitonclick()
if __name__ == "__main__":
    main()