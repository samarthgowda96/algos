def canTraverse(gas, cost, start):
    fuelRequired = cost 
    traverseLength = len(gas)
    started = False
    remaining = 0
    i = start

    while i != start or not started:
        print(i, start,started)
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
           
        i = (i+1)%traverseLength
    return True

def gasStation(gas, cost):
    for i in range(len(gas)):
        if canTraverse(gas, cost, i):
            return i
       
        

    return -1

gas = [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]
print(gasStation(gas, cost))

 