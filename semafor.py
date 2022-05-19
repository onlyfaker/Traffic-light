import time

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
