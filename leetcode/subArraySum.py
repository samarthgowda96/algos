def subArray(arr,total):
    dic= {0:1}
    length= len(arr)
    count=0
    s=0

    """ for i in range(len(arr)):
        if i==0:
            temp=0+arr[i]
            res.append(temp)
        else:
            temp= arr[i-1]+arr[i]
            res.append(temp) """
    for i in arr:
        s= s+i
        if s-total in dic:
            count+= dic[s-total]
        if s in dic:
            dic[s]+=1
        else:
            dic[s]=1

    return count
        
         



    
  


arr=[1,3,4,4]
total=8
print(subArray(arr,total))