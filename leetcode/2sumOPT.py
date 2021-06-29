def twoSum(nums,tar):
    book={}
    for i in range(len(nums)):
        temp= tar-nums[i]
        if nums[i] not in book:
            book[temp]=i
        else:
            return book[nums[i]],i

nums=[2,7,11,15]
print(twoSum(nums,9))

