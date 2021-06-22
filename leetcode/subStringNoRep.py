def subString(string):
    if len(string)==0:return 0
    dic={}
    maxLength=start=0
   
    for i in range(len(string)):
      
        if string[i] in dic and start <=dic[string[i]]:
            start= dic[string[i]]+1
        else:
            maxLength= max(maxLength,i-start+1)
        dic[string[i]]=i
    print(dic)
    return maxLength

string="asasss"
print(subString(string))