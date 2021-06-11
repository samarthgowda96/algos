# Implement a merge sort with recursion


items = [10,99,45,1,69,76,100,23]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i<len(leftarr) and j<len(rightarr):
            if leftarr[i]< rightarr[j]:
                dataset[k]=leftarr[i]
                i=i+1
            else:
                dataset[k]=rightarr[j]
                j=j+1
            k=k+1



        # TODO: if the left array still has values, add them
        while i<len(leftarr):
            dataset[k]=leftarr[i]
            i=i+1
            k=k+1


        # TODO: if the right array still has values, add them
        while j<len(rightarr):
            dataset[k]=rightarr[j]
            j=j+1
            k=k+1



# test the merge sort with data
print(items)
mergesort(items)
print(items)

def mergeSort(arr):
    mid=len(arr)//2
    leftarr=arr[:mid]
    rightarr=arr[mid:]
    
    i=0
    j=0
    k=0
    
    while i<len(leftarr) and j<len(rightarr):
        if leftarr[i]<rightarr[j]:
            arr[k]=leftarr[i]
            i=i+1
        else:
            arr[k]=rightarr[j]
            j=j+1
        k=k+1
        
    while i<len(leftarr):
        arr[k]=leftarr[i]
        i=i+1
        k=k+1
    while j<len(rightarr):
        arr[k]=rightarr[j]
        j=j+1
        k=k+1
    return arr

arr=[4,7,2,0,5,1,10]
print(mergeSort(arr))