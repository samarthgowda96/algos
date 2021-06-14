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

def findTarget(tree,k):
        diffSet= set()
        return findTargetHelper(tree, k, diffSet)
def findTargetHelper(tree,k, diffSet):
        if not tree:
            return False
        if tree.value in diffSet:
            return True
        else:
            diffSet.add((k-tree.value))
            left= findTargetHelper(tree.left,k,diffSet)
            right= findTargetHelper(tree.right,k,diffSet)
            return left or right


tree=BST(5).insert(3).insert(2).insert(4).insert(6).insert(7)
k=56
print(findTarget(tree, k))

