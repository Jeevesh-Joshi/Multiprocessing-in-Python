# Sharing Data b/w processes : Value and Array

import multiprocessing
 
def calc_square(numbers, result, v):
    v.value = 8.92
    for idx, n in enumerate(numbers):
        result[idx] = n*n
if __name__ == "__main__":
    arr = [2,3,5]

    #for creating shared variables use : multiprocessing.Array(data_type,size)
    result = multiprocessing.Array('i',3) 
    v = multiprocessing.Value('d', 0.01)
    p1 = multiprocessing.Process(target=calc_square,args=(arr,result,v))

    p1.start()
    p1.join()

    print('result = ',result[:])
    print('value = ',v.value)
    print("Job Done")

    