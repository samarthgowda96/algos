class Students:
    def __init__(self,ans,ques):
        self.ans= ans
        self.ques= ques
        self.ansLen=len(ans)
        self.quesLen= len(ques)
    
    def checkAns(self):
        res=[]

        for i in range(self.quesLen):
            tempCount=0
            for j in range(self.ansLen):
                if self.ques[i][j]==self.ans[j]:
                    tempCount+=1
            res.append(tempCount)
        for i in range(len(res)):
            statement="student {} has scored {} out of 5 right answers in the finals"
            print(statement.format(i+1,res[i]))
            
ques= [["A", "B", "C", "D", "B"],

 ["B", "B", "C","B" , "D"],

 ["D", "A", "C","D", "B"],

 ["A", "A", "C", "D", "B"],

 ["C", "B", "C", "B", "D"]]

ans=["A", "A", "C", "B", "D"]

students= Students(ans, ques)
students.checkAns()
