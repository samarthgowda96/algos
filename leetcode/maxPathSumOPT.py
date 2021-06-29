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

def maxPath(tree):
    if tree is None:
        return tree
    maximumSum=float('-inf')
    leftMax= max(0,maxPath(tree.left))
    rightMax= max(0,maxPath(tree.right))
    maximumSum= max(maximumSum,leftMax+rightMax+tree.value)

    return maximumSum


bst= BST(1)
bst.insert(2).insert(3)
print(maxPath(bst))