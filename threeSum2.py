def threeSum2(nums):
    res=[]
    if (nums is None or len(nums) ==0):
        return res

    nums.sort()
    dictionary={}
    #nums=[2,3,3,3]
    numslist=[2,1,2,3]
    print(numslist)
    for i in range(0,len(nums)):
        numslist.append(nums[i])

    for i in range(0,len(nums)):
        chosen = numslist.pop(i)
        print(chosen)
    
        numSet=set(numslist)
        print(numSet)
        ##if(numSet.co)
    
nums=[2,3,3,3]
threeSum2(nums)