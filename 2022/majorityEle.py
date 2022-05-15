""" Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array. """
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        n = len(nums)//2
        count = (Counter(nums))
        sort = dict(sorted(count.items(), key = lambda item:item[1], reverse = True) )
        for x,y in sort.items():
            if y >= n:
                return x