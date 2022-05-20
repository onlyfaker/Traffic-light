import time
import turtle

#screen, background and title
wn = turtle.Screen()
wn.title('stoplights')
wn.bgcolor('black')

#drwaing a box fpr light
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

#red circle
red = turtle.Turtle()
red.shape('circle')
red.color('grey')
red.goto(0,40)

#green circle
green = turtle.Turtle()
green.shape('circle')
green.color('grey')
green.goto(0,-40)

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
