a = "123"
ans = "632"


def find(a):
    res = ''
    total = 1
    for i in a:
      total *= int(i)

    for i in a:
      temp = total//int(i)
      res+= str(temp)

    return res


print(find(a))



      

        
