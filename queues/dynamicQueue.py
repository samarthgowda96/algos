class Queue():
    def __init__(self, limit=5):
        self.queue = []
        self.front= None
        self.rear= None
        self.limit=limit
        self.size=0
    
    def isEmpty(self):
        if self.size<= 0:
            print("queue is empty")
        else:
            print("queue is not empty")
    
    def enQueue(self,item):
        if self.size>=self.limit:
            self.resize()
        self.queue.append(item)
        if self.front is None:
            self.front=self.rear=0
        else:
            self.rear= self.size
        self.size+=1
        print("enQueue", self.queue)
    
    def deQueue(self):
        if self.size<=0:
            print("underflow")
        else:
            self.queue.pop(0)
            self.size-=1
            if(self.size==0):
                self.front=self.rear=0
            else:
                self.rear=self.size-1
        print('queue',self.queue)

    def queueRear(self):
        if self.rear is None:
            print("empty")
            raise IndexError
        return self.queue[self.rear]

    def queueFront(self):
        if self.front is None:
            print('empty')
            raise IndexError
        return self.queue[self.front]

    def size():
        return self.size

    def resize():
        newQueue= list[self.queue]
        self.limit=2*self.limit
        self.queue= newQueue

queue= Queue()
queue.queueRear()
queue.enQueue('6')
queue.enQueue('9')
queue.enQueue('10')


     


