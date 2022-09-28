import time
t0= time.process_time()
def sortedArr(arr):
    sq = {}
    res = []
    for i in arr:
        if i in sq:
            res.append(sq[i])
        else:
            temp = i * i
            sq[i] = temp
            res.append(temp)
    return res

print(sortedArr([1,21,2, 2, 4 ,4,3, 2,1]))
t1 = time.process_time() - t0
print("Time elapsed: ", t1 - t0) 


