class Queue():
    def __init__(self,limit=5):
        self.queue=[]
        self.front=None
        self.rear=None
        self.size=0

    def isEmpty(self):
        return self.size<=0

    def enQueue(self,item):
        if self.front>= self.size:
            print("Overflow!!")
        else:
            self.queue.append(item)
        if self.front is None:
            self.front=self.rear=0
        else:
            self.rear=self.size
        self.size+=1
        print("Queue after enQueue", self.queue)

    def deQueue(self):
        if self.size<=0:
            print('Underflow!')
        else:
            self.queue.pop(0)
            self.size-=1
        if self.size==0:
            self.front= self.rear=None
        else:
            self.rear= self.size-1
        print("Queue after deQueue", self.queue)


            


        
