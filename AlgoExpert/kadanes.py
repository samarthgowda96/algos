def kadanesAlgorithm(array):
    if len(array) <2:
        return array[0]
   
    kadane = [array[0]]
    maxSoFar = -1
    for i in range(1,len(array)):
        temp = kadane[i-1] + array[i]
        k = max(temp, array[i])
        if k > maxSoFar:
            maxSoFar = k
        kadane.append(k)

    return maxSoFar