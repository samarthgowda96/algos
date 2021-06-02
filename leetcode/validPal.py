class Solution:
    def isPalindrome(self,s):
        s=s.lower()
        leftidx= 0
        rightidx=len(s)-1
        while leftidx<rightidx:
            if s[leftidx].isalnum() is False:
                leftidx=leftidx+1
                continue
            if s[rightidx].isalnum() is False:
                rightidx=rightidx-1
                continue
            if s[leftidx]!=s[rightidx]:
                return False
            leftidx=leftidx+1
            rightidx=rightidx-1
        return True

sol= Solution()
s="A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))