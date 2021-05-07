class Queue():
    def __init__(self,limit=5):
        self.queue=[]
        self.limit=limit
        self.front=None
        self.rear=None
        self.size=0

    def isEmpty(self):
        if self.size<=0:
            print("Queue is Empty")
        else:
            print("Queue is  not Empty")
    def size(self):
        #print("size of queue", self.size)
        lenght= len(self.queue)
        return lenght


    def enQueue(self,item):
        if self.size>= self.limit:
            print("Overflow!!")
        else:
            self.queue.append(item)
        if self.front is None:
            self.front=self.rear=0
        else:
            self.rear=self.size
        self.size+=1
        #print(self.size())
        print("Queue after enQueue", self.queue)
        print("lenght of enQueue:",len(self.queue))

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
        print("lenght of after deQueue:",len(self.queue))
    def queueRear(self):
        if self.rear is None:
            print("queue is empty")
            raise IndexError
        return self.queue[self.rear]
    def queueFront(self):
        if self.front is None:
            print('queue is empty')
            raise IndexError
        return self.queue[self.front]
    

queue= Queue()
queue.enQueue('1')
queue.enQueue('4')
queue.enQueue('3')
queue.enQueue('10')
queue.deQueue()
queue.isEmpty()
print(queue.queueRear())
print(queue.queueFront())

            


        
