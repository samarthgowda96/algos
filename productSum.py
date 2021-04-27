def productSum(array, multiplier=1):
    sumProd =0
    for i in array:
        if type(i) is list:
            sumProd+= productSum(i, multiplier+1)
        else:
            sumProd+=i
    return sumProd*multiplier


array= [1,-1,[3,7],9]
print(productSum(array, multiplier=1))