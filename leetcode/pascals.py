def pascals(numRows):
    triangle =[]
    firstRow=[]
    firstRow.append(1)
    triangle.append(firstRow)
    for i in range(1,numRows):
        prevRow= triangle[i-1]
        row= []
        row.append(1)
        for j in range(1,i):
            row.append(prevRow[j-1]+prevRow[j])
        row.append(1)
        triangle.append(row)
    return triangle

numRows=6
print(pascals(numRows))