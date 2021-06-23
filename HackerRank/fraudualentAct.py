# def frauds(exp, d):
#     count=0
  
#     for i in range(0,len(exp)):
            
#             if(d%2)==0:
#                 j=i
#                 temp=exp[j:d+1]
#                 temp.sort()
               
#                 mid= len(temp)//2
#                 median=(temp[mid]+temp[mid-1])/2
#                 res= (2*median)
               
#                 if (len(exp)>d+1):
#                     if exp[d+1]>=res:
#                         count+=1
               
#             else:
#                 temp=exp[i:d:1]
            
#                 mid= len(temp)//2
#                 median= temp[mid]
#                 res=2*median
#                 if (len(exp)>d+1):
#                     if exp[d+1]>=res:
#                         count+=1
#             d=d+1
#     return count

import numpy as np  
def checkfrauds(exp, d):
    print ("-"*20)
    print ("Checking Fraud")
    print ("-"*20)
    
    # Initialize Alert Count Variable to 0
    alert_count = 0

    # Set n as the length of exp
    n = len(exp)

    for i in range(d, n):

        prev_d_exps = exp[i-d: i]

        if exp[i] >= np.median(prev_d_exps) * 2:
            alert_count+=1
            print('Sending Alert')

        print("{} - Prev Exp - {} - Median : {}".format( exp[i], prev_d_exps, np.median(prev_d_exps) ))

    print("n : {}".format(n))
    print ("-"*20)
    print("alert_count : {}".format(alert_count))
    return alert_count
               

#exp=[1,4,5,6,7,43,3]
exp=[10,20,30,40,50]

d= 3

checkfrauds(exp, d)