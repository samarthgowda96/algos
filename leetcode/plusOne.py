class Solution:
    def plusOne(self, digit):
        carry=0
        result=[]
        for i in range(len(digit)-1,-1,-1):
            num=digit[i]
            
            if(i==len(digit)-1):
                num+=1
                print(digit[i])
            if num + carry>9:
                if i==0:
                    result.append((num+carry)%10)
                    result.append((num+carry)//10)
                else:
                    result.append(0)
                    carry=1
            else:
                result.append(num+carry)
                carry=0

        return reversed(result)