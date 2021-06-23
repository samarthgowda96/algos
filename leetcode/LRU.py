class dll:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev= None
        self.next= None 


class LRU:
    def __init__(self,capacity):
        self.capacity = capacity
        self.head= dll(-1,-1)
        self.tail=self.head
        self.hash={}
        self.length=0

    def get(self,key):
        if key not in self.hash: 
            return -1
        node = self.hash[key]
        val=node.val
        while node.next:
            node.prev.next=node.next
            node.next.prev= node.prev
            self.tail.next= node
            node.prev= self.tail
            node .next =None
            self.tail= node 
        print(self.hash)
        return val

    def put(self, key, val):
        if key in self.hash:
            node=self.hash[key]
            node.val= val
            while node.next:
                node.prev.next=node.next
                node.next.prev= node.prev
                self.tail.next= node
                node.prev= self.tail
                node .next =None
                self.tail= node 
        else:
            node=dll(key,val)
            self.hash[key]= node
            self.tail.next=node
            node.prev=self.tail 
            self.tail= node 
            self.length+=1
            if self.length>self.capacity:
                remove= self.head.next.next
                self.head.next= self.next.next
                sel.head.next.prev= self.head
                del self.hash[remove.key]
                self.length-=1

lru=LRU(6)
print(lru.get(1))
lru.put(2,4)
print(lru.get(2))
print(lru.get(1))