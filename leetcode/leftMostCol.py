def leftMost(mat):
    n= len(mat)
    m=len(mat[0])

    col=-1
    for j in range(m):
        for i in range(0,m):
             if mat[i][j]==1:
                col=j 
                break
                break
       
    return col
    

mat=[[0,0],[1,1]]
print(leftMost(mat))