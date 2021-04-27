def smallestDiff(array1,array2):

    listt=[]
    for i in range(len(array1)):
        firstArray= array1[i]
        for j in range(len(array2)):
            secondArray= array2[j]
            
            if(firstArray<secondArray):
                res= secondArray-firstArray
                listt.append(res)
            else:
                res= firstArray-secondArray
                listt.append(res)
            #abs(res)
            listt.sort()
            print(listt)
            
            res= listt[0]

    return res
array1=[-1, 5, 1, 20, 23, 3]
array2=[1, 134, 135, 15, 17]

print(smallestDiff(array1,array2))