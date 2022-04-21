from collections import Counter
class Solution:
    def rotate(self, matrix):
        #return matrix
        res = []

        for i in range(len(matrix)-1,-1,-1):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[i][j])
            res.append(temp)
        return res
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]

sol = Solution()
print(sol.rotate(matrix))
