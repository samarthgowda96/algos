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
def pruneTree(root):
    if root is None: return
    return root if  containsOne(root) else None

def containsOne(root):
    if root is None: return

    leftContains= containsOne(root.left)
    rightContains=containsOne(root.right)

    if not leftContains:
        root.left= None
    if not rightContains:
        root.right=None

    return  root.value==1 or leftContains or rightContains 

root= BST(1).insert(0).insert(0).insert(1)
print(containsOne(root))