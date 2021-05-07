""" def reversingQueueUsingTwoStacks(arr):
    stack1 =[]
    stack2=[]
    
    for i in range(len(arr)):
        stack1.append(arr[i])
        print(stack1)
    if(len(stack2)==0):
        for i in range(len(stack1)):
            stack2.append(stack1[i])

    for i in range(len(stack2)):
        print(stack2.pop())
    

arr=[1,2,3,4,5]
(reversingQueueUsingTwoStacks(arr)) """

class Queue():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enQueue(self,item):
        self.stack1.append(item)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
queue=Queue()
for i in range(10):
    queue.enQueue(i)
for i in range(10):
    print(queue.dequeue())


