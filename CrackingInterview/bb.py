def matchingBracks(s):
    openingBracket={"{",'(',"["}
    closingBracket={"}",")","]"}
    matchingBrackets={")":"(","]":"[","}":"{"}
    stack1=[]
    closing=""
    
    for i in s:
        if i in openingBracket:
            stack1.append(i)
        if i in closingBracket:
            if len(stack1)==0:
                return False    
            if matchingBrackets[i]== stack1[-1]:
                stack1.pop()  
    if len(stack1)==0:
        return True
    else:
        return False


s="(())"
print(matchingBracks(s))