from collections import Counter
class Strings():
    def isUnique(self,string):
        if(len(set(string))==len(string)):
            return True
        else:
            return False
    def checkPerm(self,string1,string2):
        stringCount1= Counter(string1)
        stringCount2= Counter(string2)
        for i in string1:
            boo=False
            if(stringCount1[i]==stringCount2[i]):
                boo=True
        return boo

    def URLify(self,string,l):
        new=string[:l]
        finalString =new.replace(' ','%20')
        return (finalString)




s=Strings()
#print(s.checkPerm('sam','sam'))
#print(s.isUnique('sam'))
print(s.URLify('Mr John    Smith    ',13))