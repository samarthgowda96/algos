def kthLargestElement(arr,k):
    for i in range(k):
        highest = max(arr)
        arr.remove(highest)
    return max(arr)
k = 2
arr = [20,10,78,63,3,7 ,89,6]

print(kthLargestElement(arr,k))
