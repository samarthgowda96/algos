def searchInSortedMatrix(matrix, target):
    # Write your code here.
    i = 0
    j = len(matrix[0]) - 1
    while j >= 0:
        if matrix[i][j] == target:
            return i, j
        elif matrix[i][j] > target:
            j = j - 1
        else:
            i = i + 1
    return -1,-1
        
m = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
]

print(searchInSortedMatrix(m, 42))