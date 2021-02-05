def countdown(x):
    if(x==0):
        print("done!")
        return
    else:
        print('x=',x)
        countdown(x-1)

countdown(4)

def power(num,pwr):
    if pwr==0:
        return 1
    else:
        return num*power(num, pwr-1)
print(power(3,2))
        



def fact(x):
    if(x==0):
        
        return 1
    else:
        return x * fact(x-1)
print(fact(2))


