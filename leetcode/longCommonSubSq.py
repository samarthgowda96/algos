def longCommonSubSq(text1,text2):
    n= len(text1)
    m=len(text2)
    dp=[]
    for z in range(n+1):
        dp.append([0]*(m+1))
    book={}
    
    temp=[]
    res=[]

    for i in range(n):
        for j in range(m):
            
            if (text1[i]==text2[j]):
                temp.append(text1[i])
            

                
                dp[i+1][j+1]=dp[i][j]+1
                res.append(dp[i+1][j+1])
            
            else:
                dp[i+1][j+1]= max(dp[i][j+1],dp[i+1][j])
                res.append( dp[i+1][j+1])
    for i in range(len(dp)):
        print(dp[i])
    

   

    
            
 

    return dp[-1][-1]


text2="ab"
text1="dc"
print(longCommonSubSq(text1,text2))
