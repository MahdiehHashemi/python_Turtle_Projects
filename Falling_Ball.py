#Falling Ball

from turtle import *
import random
frame = Turtle()
dish = Turtle()
circle = Turtle()
triangle = Turtle()
square = Turtle()
score = Turtle()
gcircle = Turtle()
gtriangle = Turtle()
gsquare = Turtle()
guide1 = Turtle()
guide2 = Turtle()
guide3 = Turtle()


dish.hideturtle()
dish.penup()
dish.goto(0,-300)
dish.showturtle()
dish.shape("square")
dish.shapesize(1,3)

circle.hideturtle()
circle.penup()
circle.goto(0,300)
circle.showturtle()
circle.shape("circle")
triangle.shape("triangle")
triangle.penup()
square.penup()
square.shape("square")
circle.shapesize(2)
triangle.shapesize(2)
square.shapesize(2)
def move_right():
    dish.setheading(0)
def move_left():
    dish.setheading(180)

onkey(move_right,"Right")
onkey(move_left,"Left")
listen()


frame.hideturtle()
frame.speed(0)
frame.pencolor("medium aquamarine")
frame.penup()
frame.goto(350,320)
frame.pendown()
frame.pensize(4)
frame.right(90)
frame.forward(640)
frame.right(90)
frame.forward(700)
frame.right(90)
frame.forward(640)
frame.right(90)
frame.forward(700)
frame.penup()
frame.left(180)
frame.forward(4)
frame.left(90)
frame.forward(4)
frame.pendown()
frame.color("tomato")
frame.forward(633)
frame.right(90)
frame.forward(55)
frame.right(90)
frame.forward(633)
frame.right(90)
frame.forward(55)
frame.pendown()

score.hideturtle()
score.penup()
score.goto(300,220)
sc = 0
score.write("Your \nScore \nis: \n"+ str(sc),font=10)

gcircle.hideturtle()
gcircle.shape("circle")
gcircle.shapesize(1)
gcircle.penup()
gcircle.goto(320,170)
gcircle.showturtle()
gcircle.color("light pink")

guide1.hideturtle()
guide1.speed(0)
guide1.pensize(2)
guide1.pencolor("maroon")
guide1.penup()
guide1.goto(318,150)
guide1.pendown()
guide1.right(90)
guide1.forward(15)
guide1.penup()
guide1.left(90)
guide1.forward(5)
guide1.pendown()
guide1.left(90)
guide1.forward(15)
guide1.penup()
guide1.left(180)
guide1.forward(35)
guide1.right(90)
guide1.forward(10)
guide1.write("+1",font=8)

gtriangle.hideturtle()
gtriangle.shape("triangle")
gtriangle.shapesize(1)
gtriangle.penup()
gtriangle.goto(320,70)
gtriangle.showturtle()
gtriangle.color("salmon")

guide2.hideturtle()
guide2.speed(0)
guide2.pensize(2)
guide2.pencolor("maroon")
guide2.penup()
guide2.goto(318,50)
guide2.pendown()
guide2.right(90)
guide2.forward(15)
guide2.penup()
guide2.left(90)
guide2.forward(5)
guide2.pendown()
guide2.left(90)
guide2.forward(15)
guide2.penup()
guide2.left(180)
guide2.forward(35)
guide2.right(90)
guide2.forward(10)
guide2.write("-3",font=8)

gsquare.hideturtle()
gsquare.shape("triangle")
gsquare.shapesize(1)
gsquare.penup()
gsquare.goto(320,-30)
gsquare.showturtle()
gsquare.color("rosy brown")

guide3.hideturtle()
guide3.speed(0)
guide3.pensize(2)
guide3.pencolor("maroon")
guide3.penup()
guide3.goto(318,-50)
guide3.pendown()
guide3.right(90)
guide3.forward(15)
guide3.penup()
guide3.left(90)
guide3.forward(5)
guide3.pendown()
guide3.left(90)
guide3.forward(15)
guide3.penup()
guide3.left(180)
guide3.forward(35)
guide3.right(90)
guide3.forward(10)
guide3.write("+5",font=8)


def color():
    r = random.random()
    g = random.random()
    b = random.random()
    circle.color(r,g,b)

    r2 = random.random()
    g2 = random.random()
    b2 = random.random()
    triangle.color(r2,g2,b2)

    r3 = random.random()
    g3 = random.random()
    b3 = random.random()
    dish.color(r3,g3,b3)

    r4 = random.random()
    g4 = random.random()
    b4 = random.random()
    square.color(r4,g4,b4)

s = 10
color()

while True:
    y = 310
    x = random.randint(-350,295)
    circle.goto(x,y)

    y2 = 310
    x2 = random.randint(-350,295)
    triangle.goto(x2,y2)
    
    y3 = 310
    x3 = random.randint(-350,295)
    square.goto(x3,y3)
    while dish.xcor() < 350:
        dish.forward(s)

        y = y - 3
        circle.goto(x,y)
        y2 = y2 - 6
        triangle.goto(x2,y2)
        y3 = y3 - 5
        square.goto(x3,y3)

        if dish.distance(circle)<20:
            sc = sc + 1
            score.clear()
            score.write("Your \nScore \nis: \n"+ str(sc),font=10)
            circle.hideturtle()
            y = 310
            x = random.randint(-350,295)
            circle.goto(x,y)
            circle.showturtle()
            s = s + 0.2
            color()
        elif dish.distance(triangle)<20:
            sc = sc - 3
            score.clear()
            score.write("Your \nScore \nis: \n"+ str(sc),font=10)
            triangle.hideturtle()
            y2 = 310
            x2 = random.randint(-350,295)
            triangle.goto(x2,y2)
            triangle.showturtle()
            s = s + 0.2
            color()
        elif dish.distance(square)<20:
            sc = sc + 5
            score.clear()
            score.write("Your \nScore \nis: \n"+ str(sc),font=10)
            square.hideturtle()
            y3 = 310
            x3 = random.randint(-350,295)
            square.goto(x3,y3)
            square.showturtle()
            s = s + 0.2
            color()

        if dish.xcor() > 295 or dish.xcor() < -350 or dish.ycor() > 295 or dish.ycor() < -350:
            dish.goto(0,-300)
        elif circle.ycor() < -310:
            circle.hideturtle()
            y = 310
            x = random.randint(-350,295)
            circle.goto(x,y)
            circle.showturtle()
        elif triangle.ycor() < -310:
            triangle.hideturtle()
            y2 = 310
            x2 = random.randint(-350,295)
            triangle.goto(x2,y2)
            triangle.showturtle()
        elif square.ycor() < -310:
            square.hideturtle()
            y3 = 310
            x3 = random.randint(-350,295)
            square.goto(x3,y3)
            square.showturtle()
            
    break

mainloop()


#while True:
#    y = 310
#    x = random.randint(-350,295)
#    circle.goto(x,y)
#    y2 = 310
#    x2 = random.randint(-350,295)
#    triangle.goto(x2,y2)
#    while dish.xcor() < 350:
#        dish.forward(s)
#        y = y - 3
#        circle.goto(x,y)
#        y2 = y2 - 4
#        triangle.goto(x2,y2)
#        if dish.distance(circle)<20:
#            y = 310
#            x = random.randint(-350,295)
#            circle.hideturtle()
#            circle.goto(x,y) 
#            circle.showturtle()
#            s = s + 0.2
#            color()
#        elif dish.distance(triangle)<20:
#            y2 = 310
#            x2 = random.randint(-350,295)
#            triangle,hideturtle()
#            triangle.goto(x2,y2)     
#            triangle.showturtle()
#            s = s + 0.2
#            color()
#        if dish.xcor() > 295 or dish.xcor() < -350 or dish.ycor() > 295 or dish.ycor() < -350:
#            dish.goto(0,-300)
#        elif circle.ycor() < -310:
#            circle.hideturtle()
#            y = 310
#            x = random.randint(-350,295)
#            circle.goto(x,y)
#            circle.showturtle()
#        elif triangle.ycor() < -310:
#            triangle.hideturtle()
#            y2 = 310
#            x2 = random.randint(-350,295)
#            triangle.goto(x2,y2)
#            triangle.showturtle()
            
#    break
