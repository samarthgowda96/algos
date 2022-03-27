def findFirstLastIDX(arr, target):
    res = []
    for i in range(len(arr)):
        if arr[i] == target:
            firstIdx = i
            res.append(firstIdx)
            for j in range(i+1, len(arr)):
                if arr[j] != target:
                    lastIdx = j - 1
                    res.append(lastIdx)
                    return res
        
    return [-1,-1]
print(findFirstLastIDX([2,3,3,3,5,4], 5))






      
