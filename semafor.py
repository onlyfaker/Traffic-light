import time

start_time = time.time()
seconds = 1
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time == seconds:
    	print("red")
    	seconds=10
    	continue
    current_time2 = time.time()
    elapsed_time2 = current_time2 - start_time
    
    if elapsed_time2 == seconds:
    	print("yellow")
    	seconds=2
    	continue
    current_time3 = time.time()
    elapsed_time3 = current_time3 - start_time
    if elapsed_time3==seconds:
        print('green')
        seconds=10
        continue
    current_time4 = time.time()
    elapsed_time4 = current_time4 - start_time
    if elapsed_time4 == seconds:
        print("red")
        seconds=1