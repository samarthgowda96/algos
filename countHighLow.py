def countLowHigh(numlist):
   #high_list = list(filter(lambda n: n > 50 or n % 3 == 0, numlist))
   high_list = list(filter(lambda n:n>50 or n%3 == 0,numlist))
   low_list = list(filter(lambda n:n<=50 and not n%3 == 0,numlist))
   return [len(high_list),len(low_list)]

numlist=[20,1,50,233,40,22,3]
print(countLowHigh(numlist))