def eliminationGame(n):
    lst = list(range(1,n+1))
    while len(lst) !=1:
        for i in range(0,len(lst),2):
            print(i)
            lst[i] = ''
        lst = list(filter(None, lst))
        
    return lst


print(eliminationGame(9))
