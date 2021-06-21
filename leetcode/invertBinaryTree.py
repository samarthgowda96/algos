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

def invertTree(tree,res):
        
        if tree is not None:
        
            tree.left, tree.right= invertTree(tree.right,res), invertTree(tree.left,res)
            
       
        return res



tree= BST(1).insert(6).insert(3).insert(5)
res=[]

print(invertTree(tree,res))

    