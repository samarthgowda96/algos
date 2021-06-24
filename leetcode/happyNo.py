def happyNo(num): 
    seen=set()
    while sqsum(num) not in seen:
        total= sqsum(num)
        if total==1:
            return True
        else:
            seen.add(total)
            num=total
        return False
def sqsum(num):
    res=0
    while num>0:
        firstNum= num//10

        secondNum= num%10
        

        res= (firstNum*firstNum)+(secondNum*secondNum)
        num=num//10
    return res

print(happyNo(19))
