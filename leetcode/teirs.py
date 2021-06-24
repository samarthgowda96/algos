class BST:
    def __init__(self,value):
        self.value= value
        self.children={}
        self.endHere= False
class Trie:
    def __init__(self):
        self.parent=BST(None)
    def insert(self, word):
        parent=self.parent
        for i,char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = BST(char)
        parent= parent.children[char]
        if i == len(word)-1:
            parent.endhere= True
    def search(self, word):
        parent= self.parent
        for char in word:
            if char not in parent.children:
                return False
            else:
                parent= parent.children[char]
        return parent.endhere

    def startWith(self, word):
        parent = self.parent
        for char in word:
            if char not in parent.children:
                return False
            else:
                parent= parent.children[char]
        return True


             
tree=Trie()
tree.insert('ssaas')
print(tree.search("ss"))

                 