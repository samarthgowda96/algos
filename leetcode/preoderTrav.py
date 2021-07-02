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


def preOrder(tree,res):
    if tree is  not None:
       
        res.append(tree.value)
        preOrder(tree.left,res)
        preOrder(tree.right,res)
    return res

tree=BST(5).insert(3).insert(2)
res=[]
print(preOrder(tree,res))





