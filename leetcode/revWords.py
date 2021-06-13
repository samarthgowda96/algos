def revWords(string):
    inword=False
    res=[]
    string.split(" ")
    idx=0
    for i in range(0,len(string)):
        if(string[i]!= " "):
            if ( not inword and len(res)>0):
                res.append(" ")
            inword=True
            res.insert(idx, string[i])
        elif(inword):
            idx = len(string)+1
            inword= False
    return " ".join(res)

string="the sky is blue"
print(revWords(string))