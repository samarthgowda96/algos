def sqSumMatrice(m):
    n=len(m)
    x=len(m[1])
  
    count=0
    dp= [[0]*(x+1) for z in range(n+1)]
   
    for i in range(1,  n+1):
        for j in range(1,x+1):
        
            if m[i-1][j-1]==1:
                dp[i][j]= 1+ min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
                count+=dp[i][j]
    return count

    
m=[[0 ,1, 1, 0],
    [ 0, 0 ,0, 0]]
print(sqSumMatrice(m))
