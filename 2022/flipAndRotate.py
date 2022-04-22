class Solution:
    def flipAndInvertImage(self, image):
        res = []
        for i in range(len(image)):
            new =image[i][::-1]
            for i in range(len(new)):
                if new[i] == 1:
                    new[i] = 0
                else:
                    new[i]=1 
            res.append(new)
            
        return res

image = [[1,1,0],[1,0,1],[0,0,0]]
sol = Solution()
print(sol.flipAndInvertImage(image))