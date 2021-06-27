def maxSubCircularArray(arr):
    length= len(arr)
    k1=kandane(arr)
   
    circularTotal=0
    for i in range(length):
        circularTotal=circularTotal+ arr[i]
        arr[i]=-arr[i]
    k2=kandane(arr)
    
    circularTotal=circularTotal+k2
    if circularTotal>k1 and circularTotal !=0:
        return circularTotal
    else:
        return k1

def kandane(arr):
    currMax= arr[0]
    maxSum= arr[0]
    for i in arr[1:]:
        currMax=max(i, currMax+i)
        maxSum= max(currMax,maxSum)
    return maxSum

arr=[5,-3,5]
print(maxSubCircularArray(arr))