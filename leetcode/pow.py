class Solution:
    def pow(self, x, n):
        if n==0:
            return 1
        if(n<0):
            return 1/self.pow(x,-n)
        half= self.pow(x,n/2)
        if(n%2==0):
            return half*half 
        else:
            return x*half*half
sol= Solution()
x = 2.00000
n = 10

print(sol.pow(x,n))