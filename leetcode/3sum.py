class solution:
    def threeSum(self,nums):
        length= len(nums)
        nums.sort()
        stack=[]
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=length-1
            while left<right:
                currentSum= nums[i]+nums[left]+nums[right]
                if currentSum <0:
                    left=left+1
                elif currentSum>0:
                    right= right-1
                else:
                    stack.append((nums[i],nums[left],nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return stack

sol= solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

