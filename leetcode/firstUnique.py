class firstUnique():
    def __init__(self,nums):
        self.q=[]
        self.freq={}
        for i in nums:
            self.add(i)
       
    def showFirstUnique(self):
        while len(self.q)>0 and self.freq[self.q[0]]>1:
            self.q.pop(0)
        if len(self.q)==0:
            return -1
        else:
            return self.q[0]




    def add(self,val):
        
            if val in self.freq:
                self.freq[val]+=1
            else:
                self.freq[val]=1
                self.q.append(val)
nums=[1,13,2]
firstUnique= firstUnique(nums)  
print(firstUnique.showFirstUnique())  

print(firstUnique.showFirstUnique())  


 