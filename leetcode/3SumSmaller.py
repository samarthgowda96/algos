def threeSumSmaller(nums,target):
    nums.sort()
    res=[]
    for i in range(len(nums)-1):
        if nums[i]>target:
            break
        else:
            
            ress=nums[i]+nums[i+1]+(nums[len(nums)-1])
            print(ress)
            if ress<target:
                temp=[]
                temp.append(nums[i])
                temp.append(nums[i+1])
                temp.append(nums[len(nums)-1])
                res.append(temp)
    print(res)


nums=[-2, 0, 1, 3]
target=2
threeSumSmaller(nums,target)






            