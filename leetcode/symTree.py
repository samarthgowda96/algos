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

def isMirror(tree1, tree2):
    if tree1 is None and tree2 is None: return True
    if tree1 is None or tree2 is None: return False

    return (tree1.value==tree2.value) and isMirror(tree1.left, tree2.right) and isMirror(tree1.right,tree2.left)


tree = BST(1).insert(2).insert(2)
print(isMirror(tree,tree))



