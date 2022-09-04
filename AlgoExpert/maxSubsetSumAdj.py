def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) > 1:
        maxSums = [array[0], max(array[1],array[0])]
    elif len(array)==1:
        return array[0]
    else:
        return 0
    for i in range(2, len(array)):
        temp = 0
        maxTemp = max(maxSums[i-1], maxSums[i-2]+array[i])
        maxSums.append(maxTemp)
    return maxSums[-1]
        
