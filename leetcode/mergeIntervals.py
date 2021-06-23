def mergeOverLappingInt(nums):
    nums.sort(key=lambda x:x[0])
    res=[]
    i=1
    while i<len(nums):
        if nums[i][0]<=nums[i-1][1]:
            nums[i-1][0]= min(nums[i-1][0],nums[i][0])
            nums[i-1][1]= max(nums[i-1][1],nums[i][1])
            nums.pop(i)
        else:
            i=i+1
    print(nums)



nums=[[1,3],[8,10],[2,6]]
mergeOverLappingInt(nums)