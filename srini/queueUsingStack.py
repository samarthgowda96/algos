class Stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        

    def enQueue(self,item):
        if len(self.stack1) ==0:
            self.stack1.append(item)
        else:
            for i in range(len(self.stack1)):
                temp=self.stack1.pop()
                self.stack2.append(temp)
            self.stack1.append(item)

            for i in range (len(self.stack2)):
                temp= self.stack2.pop()
                self.stack1.append(temp)
        return self.stack1

   

    def deQueue(self):
        if len(self.stack1)==0:
            return []
        temp= self.stack1.pop()
        return temp



stack=Stack()
print(stack.enQueue(2))
print(stack.enQueue(3))
print(stack.enQueue(4))
print(stack.deQueue())
