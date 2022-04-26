class MyHashSet:

    def __init__(self):
        self.hashSet = []
        

    def add(self, key: int) -> None:
        if key in self.hashSet:
            return self.hashSet
        else:
            self.hashSet.append(key)
        
        
        

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)
            return self.hashSet
        return False
        

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)