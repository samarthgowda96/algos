def canTraverse(gas, cost):
    n = len(gas)
    start = 0
    idx = 0
    totalRemaining =0
    while start != n:
        for j in range(start, n):
            totalRemaining += gas[j] - cost[j]
            if totalRemaining < 0:
                totalRemaining = 0
                idx = j+1
                start = j+1
            
            else:
                start+=1
        

        
    return idx
gas = [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]
print(canTraverse(gas, cost))

            
 