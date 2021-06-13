import math
def postOffices(you,postOffice):
    res=[]
    idx=[]
    for i in range(len(postOffice)):
        temp=math.sqrt((you[0]-postOffice[i][0])*(you[0]-postOffice[i][0])+((you[1]-postOffice[i][1])*(you[1]-postOffice[i][1])))
        res.append(temp)
    tempValue= max(res)
    res.sort()
    
    #print(tempValue)
    for i in range(len(res)):
        if tempValue < res[i]:
            tempValue= res[i]
            idx.append(i)
        
    return res[0:3]
        



you =[0, 0]
postOffice=[[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
print(postOffices(you,postOffice))

