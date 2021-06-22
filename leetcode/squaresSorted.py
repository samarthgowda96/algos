def squaresSorted(nums):
    res=[]
    for i in range(len(nums)):
        temp= abs(nums[i]*nums[i])
        res.append(temp)
    return sorted(res)

nums=[-4,-1,-2]
print(squaresSorted(nums))
