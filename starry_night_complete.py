import turtle as t
import random as r
t.bgcolor('black')
t.shape('turtle')
t.speed(0)
t.colormode(255)
for j in range(1,80):
    t.penup()
    t.goto(r.randint(-260,260),r.randint(-260,260))
    t.pendown()
    t.begin_fill()
    t.pencolor('yellow')
    t.fillcolor(r.randint(1,255),r.randint(1,255),r.randint(1,255))
    d=r.randint(2,5)
    d=2*d+1
    l=r.randint(20,70)
    for i in range(1,d+1):
        t.forward(l)
        t.right(180-180/d)
    t.end_fill()    
t.mainloop()
