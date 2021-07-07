def stringShifts(s,arr):
    moveLeft=0

    for direc, amt in arr:
        if direc==0:
            moveLeft= moveLeft+amt
        else:
            moveLeft=moveLeft-amt
    moveLeft= moveLeft%len(s)
    return s[moveLeft:] +s[:moveLeft]

s="iphone"
arr=[[0,1],[1,2]]
print(stringShifts(s,arr))