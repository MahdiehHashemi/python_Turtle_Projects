import random as r
import turtle as t
from playsound import playsound
l=2
a=t.Turtle()
a.shape('circle')
sc=1
a.shapesize(sc)
a.fillcolor('purple')
a.penup()

b=t.Turtle()
b.penup()
b.setx(r.randint(-200,200))
b.sety(r.randint(-200,200))
b.pendown()
b.shape('circle')
b.fillcolor('blue')
b.penup()

d=t.Turtle()
d.penup()
d.speed(0)
d.hideturtle()
d.goto(250,-250)
d.pendown()
d.pencolor("red")
d.pensize(4)
for i in range (4):
    d.backward(500)
    d.right(90)

score=t.Turtle()
score.hideturtle()
score.clear()
score.penup()
score.setpos(180, 180)
my_score=0
score.write(str(my_score), align='right', font=('Arial', 40, 'bold'))

def move_up():
    a.setheading(90)            
def move_down():
    a.setheading(270)
def move_right():
    a.setheading(0)
def move_left():
    a.setheading(180)
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
f=1
while True:
    a.forward(f)
    if a.distance(b)<20:
        f=f+.5
        sc+=0.5
        a.shapesize(sc)
        b.goto(r.randint(-200,200),r.randint(-200,200))
        score.clear()
        my_score=my_score+1
        score.write(str(my_score), align='right', font=('Arial', 40, 'bold'))
    if a.xcor()<-250 or a.xcor()>250 or a.ycor()<-250 or a.ycor()>250:
        a.backward(20)

t.mainloop()


        


