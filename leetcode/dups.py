def dup(nums):
    res=set()
    for i in range(len(nums)):
        
        if nums[i] in res:return True
        res.add(nums[i])
 
    return False


nums=[1,2,3]
print(dup(nums))