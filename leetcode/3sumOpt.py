def threeSum(numss):
    count=+1
    nums= sorted(numss)

    for i in range(len(nums)-2):
        l=i+1
        
        r=len(nums)-1
        
        while l<r:
            if nums[i]+nums[l]+nums[r]==0:
                
                count=count+1
                l=l+1
                r=r-1
            elif nums[i]+nums[l]+nums[r]<0:
                l=l+1
            else:
                r=r-1
    return count

numss = [0,0,-1,1]
print(threeSum(numss))
