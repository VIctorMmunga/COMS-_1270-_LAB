#Name:Victor Mmunga
#Date: 9/7/2025
#lab #2
#this program uses turtle library to draw my initals V and M with different colors.
import turtle   

wn = turtle.Screen()
wn.title("initials: V M")
wn.bgcolor("lightblue")
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(5)
pen.color("red", "yellow")  
pen.begin_fill()
pen.penup()
pen.goto(-150, 50)  
pen.pendown()
pen.setheading(-70) 
pen.forward(150)
pen.setheading(70)  
pen.forward(150)
pen.end_fill()

pen.penup()
pen.goto(50, -100)
pen.pendown()
pen.color("green", "pink")  
pen.begin_fill()
pen.setheading(90)   
pen.forward(200)
pen.setheading(-45)
pen.forward(100)
pen.setheading(45)   
pen.forward(100)
pen.setheading(-90)  
pen.forward(200)
pen.end_fill()
pen.hideturtle()
wn.mainloop()

