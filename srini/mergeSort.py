def mergeSort(arr):
    if len(arr)>1:
        mid= len(arr)//2
        leftarr= arr[:mid]
        rightarr=arr[mid:]

        mergeSort(leftarr)
        mergeSort(rightarr)

        i=0
        j=0
        k=0

        while i<len(leftarr) and j<len(rightarr):
            if len(leftarr)<len(rightarr):
                arr[k]= leftarr[i]
                i=i+1
            else:
                arr[k]= rightarr[j]
                j=j+1
            k+=1

        while i<len(leftarr):
            arr[k]=leftarr[i]
            i+=1
            k+=1

        while j<len(rightarr):
            arr[k]=rightarr[j]
            j+=1
            k+=1



arr=[3,1,6,7,2]
print(mergeSort(arr))
print(arr)

    