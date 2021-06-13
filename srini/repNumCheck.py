def repNumCheck(nums):
    res=[None]
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j] and nums[i] not in res:
                res.append(nums[i])
           
               
    return res
   
    

        
        

    




nums=[1,3,4,3,1]

print(repNumCheck(nums))