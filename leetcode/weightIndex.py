import random
def weightIndex(weights):
    prefixSum=[]
    total=0
    for i in weights:
        total+=i
        prefixSum.append(total)
    total=total
  

    rand= random.random()*total
    low=0
    high= len(prefixSum)
    while low<high:
        mid=low+high//2
        if rand >prefixSum[mid]:
            low=mid+1
        else:
            high=mid
            
    return low

 
weights=[1,2,4]
print(weightIndex(weights))
