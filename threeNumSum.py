def threeNumSum(array, total):
    array.sort()
    listt=[]
    for i in range(len(array)-2):
        leftindex=i+1
        rightindex=len(array)-1
        while leftindex<rightindex:
            summ= array[i]+array[leftindex]+array[rightindex]
            if(summ==total):
                listt.append(array[i])
                listt.append(array[leftindex])
                listt.append(array[rightindex])
                leftindex+=1
                rightindex+=1
            elif summ<total:
                leftindex+=1
            elif summ>total:
                rightindex-=1
        return listt
    

array=[12, 3, 1, 2, -6, 5, -8, 6]
total=0
print(threeNumSum(array,total))