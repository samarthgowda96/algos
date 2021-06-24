def lengthOfLongSubString(string):
    count=[None]*256
    i=0
    maxLen=0
    for j in range(len(string)-1):
        if count[string[j]==0]:
            count[string[j]]+=1
            maxLen = max(maxLen,j-i+1)
        else:
           count[string[i+1]]-=1
    return maxLen

string="abcabcbb"
print(lengthOfLongSubString(string))