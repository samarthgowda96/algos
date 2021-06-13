class Solution():
    def revEachWord(self,string):
        res=string.split(" ")
        rev=[]
        for i in range(len(res)):
            temp= res[i][::-1]
            rev.append(temp)
            rev.append(" ")
        return " ".join(rev)
            

sol= Solution()
print(sol.revEachWord('sams hell cat'))
    


