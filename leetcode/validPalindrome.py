# 125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join(filter(str.isalnum, s))
        rev = newS.lower()[::-1]

        if newS.lower()==rev:
            return True
        return False