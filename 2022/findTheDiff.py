class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t: 
            if i not in s: return i




s = 'abcd'
t = 'abcde'
sol = Solution()
print(sol.findTheDifference(s,t))