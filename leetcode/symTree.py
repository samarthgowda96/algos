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

def areSymmetric(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.value != root2.value: return False
    else: return areSymmetric(root1.left,root2.right) and areSymmetric(root1.right, root2.left)

def isSymmetric(root):
    if root is None:
        return True
    return areSymmetric(root.left, root.right)


def isMirror(tree1, tree2):
    if tree1 is None and tree2 is None: return True
    if tree1 is None or tree2 is None: return False

    return (tree1.value==tree2.value) and isMirror(tree1.left, tree2.right) and isMirror(tree1.right,tree2.left)


#tree = BST(1).insert(2).insert(2).insert(3).insert(4).insert(4).insert(3)
root = BST(1)
root.left = BST(2)
root.right = BST(2)
root.left.left = BST(3)
root.left.right = BST(4)
root.right.left = BST(4)
root.right.right = BST(3)
print(isSymmetric(root))

#print(isMirror(tree,tree))



