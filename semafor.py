import time
import turtle

#screen, background and title
wn = turtle.Screen()
wn.title('stoplights')
wn.bgcolor('black')

#drwaing a box for light
pen = turtle.Turtle()
pen.color('green')
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30,60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

#drwaing a box2 for light
pen2 = turtle.Turtle()
pen2.color('green')
pen2.width(3)
pen2.hideturtle()
pen2.penup()
pen2.goto(-30,-70)
pen2.pendown()
pen2.fd(60)
pen2.rt(90)
pen2.fd(90)
pen2.rt(90)
pen2.fd(60)
pen2.rt(90)
pen2.fd(90)

#red circle
red = turtle.Turtle()
red.shape('circle')
red.color('grey')
red.goto(0,40)

#red circle 2
red2 = turtle.Turtle()
red2.shape('circle')
red2.color('grey')
red2.goto(0,-90)

#green circle
green = turtle.Turtle()
green.shape('circle')
green.color('grey')
green.goto(0,-40)

#green circle 2
green2 = turtle.Turtle()
green2.shape('circle')
green2.color('grey')
green2.goto(0,-140)

#yellow circle
yellow = turtle.Turtle()
yellow.shape('circle')
yellow.color('grey')
yellow.goto(0,0)

#this part of a code can be used for returning the value for the set period of time
#loop for infinite change of light
while True:
    red.color('grey')
    green.color('green')
    start_time = time.time()

    seconds = 10

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= seconds:
            green.color('grey')
            yellow.color('yellow')
            break
    start_time2 = time.time()
    seconds2 = 3.5

    while True:
        current_time2 = time.time()
        elapsed_time2 = current_time2 - start_time2

        if elapsed_time2 >= seconds2:
            yellow.color('grey')
            red.color('red')
            break
    start_time2 = time.time()
    seconds3 = 10

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time2

        if elapsed_time >= seconds:
            break
