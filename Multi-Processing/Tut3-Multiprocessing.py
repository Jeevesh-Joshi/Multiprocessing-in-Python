import time
import multiprocessing
 
result = []
def calc_square(numbers):
    global result
    print("calculate square numbers")
    for n in numbers:
        print('square:',n*n)
        result.append(n*n)
    print('result within the process = ',result)
if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))

    p1.start()
    p1.join()

    print('result outside the process= ',result)
    print("Job Done")

"""The 'result' outside and within the process(p1) is not same despite treating the 'result' array as global because everytime a new process is created a new copy of variables is created along with it either global or local. every process has its own address space. Thus program variables are not shared b/w 2 processes. Inorder to do so we need to use IPC i.e Inter Process Synchronisation."""
    