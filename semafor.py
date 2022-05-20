import time
import turtle


wn = turtle.Screen()
wn.title('stoplights')
wn.bgcolor('black')

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


while True:
    print('green')
    start_time = time.time()

    seconds = 10

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= seconds:
            print("yellow")
            break
    start_time2 = time.time()
    seconds2 = 3.5

    while True:
        current_time2 = time.time()
        elapsed_time2 = current_time2 - start_time2

        if elapsed_time2 >= seconds2:
            print("red")
            break
    start_time2 = time.time()
    seconds3 = 10

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time2

        if elapsed_time >= seconds:
            break
