
def binarySearch(array, target):
    
    left=0
    right=len(array)-1
   
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            right =mid-1
        else:
            left=mid+1
    return -1
            
print(binarySearch([2,221212,34,45,23333], 23333))