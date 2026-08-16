
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node 
        self.tail = node
        self.length = 1


    def print(self):
        temp = self.head
        dic = {}
        while temp is not None:
            print(temp.value)
           
            temp = temp.next
        return dic
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1
        return True
            

    def pop(self):
       if self.head is None or self.length==1:
           return None
       temp= self.head
       pre = self.head
       while temp is not None:
           pre = temp
           temp = temp.next
       tail = pre 
       tail.next= None
   
       return pre
    
    def prepend(self,value):
        node = Node (value)
        temp = self.head
        node.next = temp
        self.head = node
        

    def popFirst(self):
        if self.head is None or self.length==1:
           return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length-=1
        if self.length ==0:
            self.tail=None
        return temp
    
    def get(self, index):
        if index < 0 or index > self.length:
            return "invalid idx"
        temp = self.head
        i = 0
        while i < index:
            temp= temp.next
            i+=1
        return temp
    
    def setV(self, index, value):
        if index < 0 or index > self.length:
            return "invalid idx"
        temp = self.head
       
        for _ in range(index -1):
            temp = temp.next
        temp.value= value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return "invalid idx"
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    def remove(self, index):
        if index < 0 or index > self.length:
            return "invalid idx"
        if index == 0:
            return self.popFirst()
        elif index == self.length:
            return self.pop()
  
        tempPrev = self.get(index-1)
        tempRmv = self.get(index)
        tempPrev.next = tempRmv.next
        tempRmv.next = None
        self.length-=1
        return True
    

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next= before
            before = temp
            temp = after 
        self.print()

linkyList = LinkedList(4)
linkyList.append(5)
linkyList.append(6)
linkyList.append(13)
linkyList.append(98)
linkyList.popFirst()
linkyList.setV(1,100)
linkyList.insert(1,1000)
linkyList.remove(1)

print(linkyList.get(2).value)
linkyList.print()
linkyList.reverse()




