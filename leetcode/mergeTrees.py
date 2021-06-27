class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


    def insert(self, value):
        currentNode= self
        while True:
            if value < currentNode.value:
                if currentNode.left is  None:
                    currentNode.left= BST(value)
                    break
                else:
                    currentNode= currentNode.left
            else:        
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode= currentNode.right
        return self


def mergeTree(tree1, tree2):
        if not tree1:
            return tree2
        if not tree2:
            return tree1   
            
        t= BST(tree1.value+tree2.value)
        print(tree2.value)
        tree1.left=mergeTree(tree1.left,tree2.left)
        tree2.right=mergeTree(tree1.right, tree2.right)
    
        return t.value


tree1= BST(1).insert(3).insert(2).insert(5)
tree2= BST(2).insert(1).insert(3).insert(4).insert(7)

print(mergeTree(tree1,tree2))


e