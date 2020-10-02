import time
import multiprocessing
 
def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(5)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(5)
        print('cube:',n*n*n)

if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_square,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
    # You can track your processes in the task manager -> details.
    # You will see 3 processes 1 parent and the rest 2 child processes.