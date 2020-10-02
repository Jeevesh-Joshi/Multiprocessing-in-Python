import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

arr = [2,3,8,9]

# Without Multi-threading

start = time.time()

calc_square(arr)
calc_cube(arr)

end = time.time()
print("Done in : ",end-start)

# With Multi-threading

start = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

# starting the thread in parallel
t1.start()
t2.start()

# join means wait untill the respective thread is done
t1.join()
t2.join()

end = time.time()
print("Done in : ",end-start)

"""Here first the control was inside 'calc_square' and as soon as the function called sleep() the CPU became idle and started with the execution of the other function. This way when ever either of them was sleeping the control switched to the other function."""