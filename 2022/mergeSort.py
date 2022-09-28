class MergeSort:
    def merge(self, array):
        if len(array) > 1:
            mid = len(array)//2
            leftArr = array[:mid]
            rightArr = array[mid:]
            print(leftArr, rightArr)

            self.merge(leftArr)
            self.merge(rightArr)

            i=0
            j=0
            k=0

            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] < rightArr[j]:
                    array[k] = leftArr[i]
                    print(array)
                    i += 1
                
                else:
                    array[k] = rightArr[j]
                    j += 1
                k += 1
            
            while i < len(leftArr):
                array[k] = leftArr[i]
                i += 1
                k += 1
            while j < len(rightArr):
                array[k] = rightArr[j]
                j += 1
                k += 1
        return array

arr = [2,11,1,3,5]
mergeSort = MergeSort()
print(mergeSort.merge(arr))



