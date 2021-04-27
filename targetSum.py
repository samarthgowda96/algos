def targetSum(arr,n):
    array=[]
    for i in range(0,len(arr)-1):
        first=arr[i]
        for j in range(i+1,len(arr)):
            second=arr[j]
            summ=first+second
            #print(res)
            if(summ==n):
                array.append(first)
                array.append(second)
                
    return sorted(array)
print(targetSum([5, 3, -4, 8, 11, 1, -1, 6],10))

