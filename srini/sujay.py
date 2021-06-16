class Solution():

    def ascSort(self,arr):
        arr.sort()
        print("asc order",arr)

    def desSort(self,arr):
        arr.sort(reverse=True)
        print("dsc sort",arr )

    def mean(self,arr):
        total=sum(arr)
        res= total/len(arr)
        print("mean of array",res)

    def median(self,arr):
        if len(arr)%2==0:
            low=len(arr)//2
            res= (arr[low]+arr[low+1])/2
            print("median",res)
        else:
            index= len(arr)//2
            print("median", arr[index])

    def findEle(self,arr, idx):
        print("Value at ",idx,"is ",arr[idx])

    def diff(self,arr):
        total= arr[0]
        res=[]
        for i in range(len(arr)):
            if i==0:
                res.append(arr[i])
            else:
                diff = arr[i]-total
                res.append(abs(diff))
        print(res)

sol= Solution()
arr=[23,4,3,2]
idx=1
sol.findEle(arr,idx)
sol.ascSort(arr)
sol.desSort(arr)
sol.median(arr)
sol.diff(arr)





