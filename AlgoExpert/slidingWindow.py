def maxSubArrays(arr, k):
    res = []
    queue = []
    i = 0

    while (i < k):
        queue.append(arr[i])
        i +=1 
    queue.sort(reverse = True)
    res.append(queue[0])
    queue.remove(arr[0])

    while i < len(arr):
        queue.append(arr[i])
        queue.sort(reverse = True)
        res.append(queue[0])
        queue.remove(arr[i-k+1])
        i +=1

        
    
    return res
    
arr =[8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
print(maxSubArrays(arr,k))