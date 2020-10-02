# Sharing Data between Processes using Queue

import multiprocessing
 
def calc_square(numbers,q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":
    arr = [2,3,5]

    #for creating queue use : multiprocessing.Queue()
    
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square,args=(arr,q))

    p1.start()
    p1.join()

    while not q.empty():
        print(q.get())

    