import turtle

import time
def draw(turtle,degrees,lengths):
    t = turtle
    for i in range(2):
        t.forward(lengths)
        t.left(degrees)
    turtle.write("Done")
    time.sleep(0)
def draw_main(X,Y,speeds,degrees,sleeps,lengths):
    #X轴 最大350
    #Y轴 最大330

    turtle.speed(speeds)
    turtle.penup()#抬起画笔
    turtle.pensize(1)
    turtle.goto(X,Y)
    turtle.color("black")
    turtle.pendown()
    draw(turtle,degrees,lengths)
    turtle.penup()#抬起画笔

    #turtle.forward(100)
    turtle.color("red")
    turtle.write("Done")
    turtle.home()
    time.sleep(sleeps)
speeds=10
sleeps=0
sleepEnd=5
#-----------------------------------------
draw_main(-310,250,speeds,-180-30,sleeps,100)
draw_main(-310,140,speeds,180-45,sleeps,100)
draw_main(-310,30,speeds,180-60,sleeps,100)
draw_main(-310,-80,speeds,180-75,sleeps,100)
draw_main(-310,-190,speeds,180-90,sleeps,100)
draw_main(-310,-300,speeds,180-105,sleeps,100)
#-----------------------------------------
draw_main(-100,250,speeds,180-120,sleeps,100)
draw_main(-100,140,speeds,180-135,sleeps,100)
draw_main(-100,30,speeds,180-150,sleeps,100)
draw_main(-100,-80,speeds,180-165,sleeps,100)
draw_main(-100,-190,speeds,180-180,sleeps,100)
draw_main(-100,-300,speeds,180-195,sleeps,100)
#-----------------------------------------
draw_main(120,250,speeds,180-205,sleeps,100)
draw_main(120,140,speeds,180-220,sleeps,100)
draw_main(120,30,speeds,180-230,sleeps,100)
draw_main(120,-80,speeds,180-245,sleeps,100)
draw_main(120,-190,speeds,180-260,sleeps,100)
draw_main(120,-300,speeds,180-275,sleepEnd,100)
