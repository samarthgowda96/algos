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


def diameterOfTree(tree):
    if tree is None:
        return 0

    lheight= height(tree.left)
    rheight= height(tree.right)

    ldiameter= diameterOfTree(tree.left)
    rdiameter= diameterOfTree(tree.right)
    return max(lheight+rheight,max(ldiameter,rdiameter))

def height(tree):
    if tree is None:
        return 0
    else:
        return 1+ max(height(tree.left),height(tree.right))

tree= BST(1).insert(3).insert(2).insert(4).insert(5)
print(diameterOfTree(tree))