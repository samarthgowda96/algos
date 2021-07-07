def countingEle(arr):
    book={}
    for i in arr:
        book[i]=1
    res=0
    for i in arr:
        if i+1 in book:
            res+=1
    return res

arr=[1,2,3]
print(countingEle(arr))
   