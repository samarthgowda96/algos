def threeSumClosest(nums,target):
    nums.sort()
    total=sum(nums[:3])
    for i in range(len(nums)-2):
        l=i+1
        h=len(nums-1)
        tempSum=nums[i]+nums[l]+nums[j]
        if abs(tempSum-target)<abs(total-target):
            total= tempSum
        if tempSum<target:
            l=l+1
        else:
            h=h+1
    return total

