def searchMatrix(target, matrix):
    for i in range(len(matrix)):
        for j in range(0,len(matrix)+1):
            print(i, j)
            if matrix[i][j] == target:
                pass
                #return True
    return False

matrix = [[1,2]]
target = 10

print(searchMatrix(target, matrix))