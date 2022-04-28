#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    medians =[]
    temp = []
    for i in range(len(a)):
        
        temp.append(a[i])
        temp = sorted(temp)
        if len(temp)%2 == 0:
            runningMedianTemp = (a[len(temp)//2]+a[(len(temp)//2)-1])/2
            medians.append(runningMedianTemp)
        else:
            runningMedianTemp = a[len(temp)]/2
            medians.append(runningMedianTemp)
    print(medians)
    return medians
             