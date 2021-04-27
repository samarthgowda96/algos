def fibo(n,res={}):
    if(n in res): return res[n]
    
    if(n<=2):
        return 1

    res[n]=fibo(n-1,res)+fibo(n-2,res)
    return res[n]
    
print(fibo(50))