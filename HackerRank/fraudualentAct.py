def frauds(exp, d):
    count=0
  
    for i in range(0,len(exp)):
            
            if(d%2)==0:
                j=i
                temp=exp[j:d+1]
                print(temp)
                mid= len(temp)//2
                #print(temp[mid],temp[mid-1])
                median=(temp[mid]+temp[mid-1])/2
                res= (2*median)
               
                if (len(exp)>d+1):
                    if exp[d+1]>=res:
                        count+=1
               
                
                
            else:
                temp=exp[i:d:1]
            
                mid= len(temp)//2
                median= temp[mid]
                res=2*median
               
                """ if (len(exp)>=d+1):
                    if exp[d+1]>=res:
                        count+=1 """
            d=d+1
    return count
                

               

exp=[1,4,5,6,7,43,3]
d= 2

print(frauds(exp,d))