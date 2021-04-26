def bubbleSort(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if(n[j]>n[j+1]):
                temp = n[j]
                n[j]=n[j+1]
                n[j+1]=temp
    return n

n=[2,31,40,25,20]
print(bubbleSort(n))