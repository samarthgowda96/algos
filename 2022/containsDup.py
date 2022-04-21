from collections import Counter
def containsDuplicate(nums):
        count = dict(Counter(nums))
        highest = max(count.values())
        if highest >= 2:
            return True
        return False
        

nums = [2,3,1]
print(containsDuplicate(nums))