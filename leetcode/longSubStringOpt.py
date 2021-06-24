def longSubStringOpt(string):
     if len(string)==0:return ""

     minLength= len(string[0])
     for i in range(len(string)):
         minLength=min(len(string[i]),minLength)
     i=0
     lcp=""
     while i<minLength:
         char= string[0][i]
         for j in range(0, len(string)):
             if string[j][i]!= char:
                 return lcp
         lcp=lcp+char
         i+=1
     return lcp

string=["f","flowwer","floeee"]
print(longSubStringOpt(string))



