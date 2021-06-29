def spiralMatrix(m):
    rowBegin= 0
    rowEnd=len(m)
    colBegin=0
    colEnd=len(m[0])
    res=[]

    while rowEnd>rowBegin and colEnd>colBegin:
        for i in range(colBegin,colEnd):
            res.append(m[rowBegin][i])
        for j in range(rowBegin+1,rowEnd-1):
            res.append(m[j][colEnd-1])

        if rowEnd!=rowBegin+1:
            for z in range(colEnd-1,colBegin-1,-1):
                res.append(m[rowEnd-1][z])
        if colBegin!=colEnd-1:
            for x in range(rowEnd-2,rowBegin,-1):
                res.append(m[j][colBegin])
        rowBegin+=1
        rowEnd-=1
        colBegin+=1
        colEnd-+1

    return res


m=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print(spiralMatrix(m))


