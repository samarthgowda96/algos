def fib(n,memo):
    if memo[n]!= None:
        return memo[n]
    if n==1 or n==2:
        result =1
    else:
        result= fib(n-1) + fib(n-2)
        memo[n]=result 
    return result

n= 50

print(fib(n,0))