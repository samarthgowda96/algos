def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

def selectionSort(A):

    for i in range(len(A)-1):
        minele=i
        for j in range(i+1,len(A)):
            if (A[j]<A[minele]):
                minele=j
        swap(A,minele,i)

    return A



    
A = [3, 5, 8, 4, 1, 9, -2]
print(selectionSort(A))

