import re
from collections import Counter
class Words:
    def findCommonWords(self, Text, Exclude):
        text= Text.lower()
    
        exclude=[]
        res=re.findall(r"[\w]+|[.,'!?;]", text)
        for i in range(len(Exclude)):

                exclude.append(Exclude[i].lower())

    

        newRes=[]
        for i in range(len(res)):
           
            if res[i] not in exclude:
                newRes.append(res[i])
        count= Counter(newRes)
                
        print(count.most_common(3))

       






Text="Jack and Jill went to the market to buy bread and cheese. Cheese is Jack’s and Jill’s favorite food."
Text.upper()
Exclude=["and","he","the","to","is","jack","Jill"]
words= Words()

words.findCommonWords(Text,Exclude)
