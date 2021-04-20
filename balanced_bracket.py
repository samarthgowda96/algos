def balancedBracket(string):
    openingBracket="({["
    closingBracket=")}"
    matchingBrackets={")":"(","]":"[","}":"{"}
    stack=[]
    for i in string:
        if i in openingBracket:
            stack.append(i)
        if i in closingBracket:
            if len(stack)==0:
                return False
            if stack[-1]==matchingBrackets[i]:
                stack.pop()
    if len(stack)==0:
        return True
    else:
        return False

print(balancedBracket("(()"))