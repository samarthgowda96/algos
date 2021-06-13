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


def preorder(tree,array):
   
    if tree is not None:
        array.append(tree.value)
        preorder(tree.left,array)
        preorder(tree.right,array)
    return array

test_tree = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) 
array=[]
print(preorder(test_tree,array))