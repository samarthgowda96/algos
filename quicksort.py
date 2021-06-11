# Implement a quicksort


items = [10,99,45,1,69,76,100,23]

 
def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # TODO: advance the lower index
        if lower<=upper and datavalues[lower]<=pivotvalue:
            lower=lower+1

        # TODO: advance the upper index
        if upper>= lower and datavalues[upper]>=pivotvalue:
            upper=upper-1

        # TODO: if the two indexes cross, we have found the split point
        if upper<lower: 
            done=True
        else:
            temp =datavalues[upper]
            datavalues[upper] =datavalues[lower]
            datavalues[lower] =temp
        

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper


# test the merge sort with data
print(items)
quickSort(items, 0, len(items)-1)
print(items)
