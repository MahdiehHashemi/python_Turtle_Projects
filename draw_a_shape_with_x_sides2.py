import turtle
import random
turtle.speed(5)
def drow():
    turtle.penup()
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    
    
    for i in range(sides):
        turtle.forward(length)
        turtle.right(num1)
    turtle.end_fill()
turtle.pensize(4)
turtle.hideturtle()
ans = "yes"
while ans == "yes":
    print("\n\n--------------------------------------------------------------")
    sides = int(input("\n Enter the number of sides : "))
    length = int(input("\n Enter the shape length : "))
    t = int(input("\n How many do you want to drow ? "))
    num = (sides-2) * 180
    num1 = (num // sides) - 180

    for x in range(t):
        pen_color = input("\n Do you want to choose the pen and fill color or random ? c for choose, r for random : ")

        if pen_color =="c":
                pencolor = input("\n Enter the pen color name or hex value of color : ")
                fillcolor = input("\n Enter the fill color name or hex value of color : ")
                fill_color = turtle.pencolor(pencolor)
                fill_color = turtle.fillcolor(fillcolor)
                drow()

        elif pen_color == "r":
        
                turtle.colormode(255)
                pr = random.randint(0,255)
                pg = random.randint(0,255)
                pb = random.randint(0,255)

                fr = random.randint(0,255)
                fg = random.randint(0,255)
                fb = random.randint(0,255)
                fill_color2 = turtle.pencolor(pr,pg,pb)
                fill_color2 = turtle.fillcolor(fr,fg,fb)
                drow()
        else:
            print("\n Wrong input !")

    ans = input("\n Wanna drow again ? yes/no ")

#Paniz Monazzah