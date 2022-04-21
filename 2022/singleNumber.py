from collections import Counter


class Solution:
    def singleNumber(self, nums):

        count = dict(Counter(nums))
        print(count)
        minimum = min(count, key = count.get)

        return minimum 


nums = [1,1,2,3,3,3,3,6,6,7,7]
sol = Solution()
print(sol.singleNumber(nums))

        
        

        