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
    def isSubTree(self,tree1,tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree2 is None: return True
        if tree1 is None and tree2 is not None:return False
        return isSame(tree1,tree2) or self.isSubTree(tree1.left,tree2) or self.isSubTree(tree1.right, tree2)



def isSame(tree1,tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None: 
        return False
    return tree1.value==tree2.value and isSame(tree1.left,tree2.left) and isSame(tree1.right,tree2.right)


tree1= BST(3).insert(4).insert(6).insert(1).insert(2)
tree2= BST(4).insert(1).insert(2)

print(tree2.isSubTree(tree1,tree2))