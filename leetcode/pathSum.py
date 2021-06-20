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

def pathSum(tree,total):
    if tree is None:
        return False
    nodeStackk=[]
    sumStackk=[]
    nodeStackk.append(tree)
    diff= total-tree.value
    sumStackk.append(diff)
    while ( len(nodeStackk)!=0):
       currentNode= nodeStackk.pop()
       currentSum= sumStackk.pop()
       if currentNode.left is None and currentNode.right is None and currentSum==0:
            return True
       if currentNode.left is not None:
            nodeStackk.append(currentNode.left)
            sumStackk.append(currentSum-currentNode.left.value)
        
       if currentNode.right is not None:
            nodeStackk.append(currentNode.right)
            sumStackk.append(currentSum-currentNode.right.value)

   


    return False


tree= BST(5).insert(2).insert(3)
total=10
print(pathSum(tree,total))


