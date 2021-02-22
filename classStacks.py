class Stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def push_items(self,item):
        return self.items.append(item)
    
    def pop_items(self):
        return self.items.pop()

    def last_item(self):
        return self.items[-1]
    
    def size_of_stack(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

if __name__=="__main__":
    stack= Stack()
    print(stack.is_empty())
    stack.push_items(2)
    stack.push_items(3)
    stack.push_items(1)
    stack.push_items(5)
    print(stack.is_empty())
    print(stack)
    stack.pop_items()
    print(stack)
    print(stack.size_of_stack())
    print(stack.last_item())
