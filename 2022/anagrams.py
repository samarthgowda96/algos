def checkAnagram(string1, string2):
    count1 = {}
    count2 = {}
    for i in string1:
        if i not in count1:
            count1[i] = 1
        else:
            count1[i] += 1
    for j in string2:
        if j not in count2:
            count2[j] = 1
        else:
            count2[j] += 1
            
    if count1==count2:
        return True
    return False

string1= "nameless"
string2="salesmen"
print(checkAnagram(string1,string2))
    