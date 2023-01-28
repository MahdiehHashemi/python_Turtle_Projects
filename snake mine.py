from turtle import *
import random as r
import turtle
import time
e=Turtle()
b=Turtle()
e.penup()
b.penup()
e.shape('square')
b.shape('circle')
b.goto(0,150)
e.penup()
b.penup()
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
score=0
def go_up():
    e.setheading(90)

def go_down():
    e.setheading(270)

def go_left():
    e.setheading(180)

def go_right():
    e.setheading(0)   
def left_click(x,y):
    e.color(r.random(),r.random(),r.random())   
turtle.listen()
turtle.onscreenclick(left_click,1)
turtle.onkey(go_up,"Up")
turtle.onkey(go_right,"Right")
turtle.onkey(go_left,"Left")
turtle.onkey(go_down,"Down")
segments=[e]
pen.write("Score : " +str(score), align="center",
font=("candara", 24, "bold"))
d=3
while True:
    e.forward(d)
    if e.distance(b)<20:
        d+=1
        cc=r.random()
        score=score+1
        pen.clear()
        pen.write("Score : " +str(score), align="center",
        font=("candara", 24, "bold"))
        b.goto(r.randint(-100,100),r.randint(-100,100))
        b.color(cc,0,0)
        ns=Turtle()
        ns.shape("square")
        ns.penup()
        ns.color(cc,0,0)
        segments.append(ns)
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
turtle.mainloop()