from turtle import *
import random 
import time 
bgcolor("light green")
f=1
h=2
s=0
u=Turtle ()
u.penup ()
u.shape ("circle")
u.color ("silver")
u.goto (-100,100)
kisekesh=Turtle ()
kisekesh.penup ()
kisekesh.pensize (3)
kisekesh.pencolor ("blue")
kisekesh.goto (-220,220)
for k in range (4) :
    kisekesh.pendown ()
    kisekesh.forward (440)
    kisekesh.right (90)
toomaj=Turtle ()
toomaj.penup ()
toomaj.goto (220,220)
toomaj.hideturtle ()
toomaj.write (s,font=('Arial', 40, 'bold'))
a=Turtle ()
a.shape("turtle")
a.shapesize(f)
a.color("green")
b=Turtle ()
b.penup()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
register_shape('leaf', leaf_shape)
b.shape('leaf')
b.color('green')
b.penup()
t=random.randint (1,40)
b.goto(-100,100)
a.penup()
m=Turtle ()
m.penup()
leaf = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
register_shape('leaf', leaf)
m.shape('leaf')
m.color('gold')
m.penup()
m.hideturtle()
start=time.time ()
def you_up ():
    a.setheading (90)
def you_left ():
    a.setheading (180)
def you_right ():
    a.setheading (0)
def you_dawn ():
    a.setheading (270)
onkey(you_up,"Up")
onkey(you_left,"Left")
onkey(you_right,"Right")
onkey(you_dawn,"Down")
listen()
while time.time()-start<120:
    if s<=10:
        a.shapesize (f)
        a.forward (h)
        if  a.xcor()>220 or a.ycor()>220 or a.xcor()<-220 or a.ycor()<-220 :
            a.backward (10)
        if a.distance(b)<20 :
            s+=1
            f+=0.5
            h+=0.5
            toomaj.clear ()
            toomaj.write (s,font=('Arial', 40, 'bold'))
            b.goto(random.randint (-210,210),random.randint(-210,210))
            b.fillcolor(random.random (),random.random(),random.random())
    if s>10 :
        m.showturtle()
        a.shapesize (f)
        a.forward (h)
        if  a.xcor()>220 or a.ycor()>220 or a.xcor()<-220 or a.ycor()<-220 :
            a.backward (10)
        if a.distance(b)<20 :
            s+=1
            f+=0.5
            h+=0.5
            toomaj.clear ()
            toomaj.write (s,font=('Arial', 40, 'bold'))
            b.goto(random.randint (-210,210),random.randint(-210,210))
            b.fillcolor(random.random (),random.random(),random.random())
        if a.distance(m)<20 :
            s+=3
            toomaj.clear ()
            toomaj.write (s,font=('Arial', 40, 'bold'))
            m.hideturtle()
            m.goto(random.randint (-210,210),random.randint(-210,210))
            m.showturtle()
    if a.distance(u)<20 :
        s-=1
        f-=0.5
        h-=0.5
        toomaj.clear ()
        toomaj.write (s,font=('Arial', 40, 'bold'))
        u.goto(random.randint (-210,210),random.randint(-210,210))
toomaj.goto (-150,0)
toomaj.write ("your score is "+str(s),font=('Arial', 40, 'bold'))
mainloop ()