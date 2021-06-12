class BST:
    def __init__(self,value):
        self.value= value
        self.right= None
        self.left = None
    def insert(self, value):
        currentNode= self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left= BST(value)
                    break
                else:
                    currentNode= currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right= BST(value)
                    break
                else:
                    currentNode= currentNode.right
        return self


def preorder(tree, array):
        if tree is not None:
          
            array.append(tree.value)
            preorder(tree.left, array)
            preorder(tree.right, array)
        return array

def inorder(tree,array):
        if tree is not None:
            inorder(tree.left,array)
            array.append(tree.value)
            inorder(tree.right, array)
        return array
def postorder(tree,array):
        if tree is not None:
            postorder(tree.left, array)
            postorder(tree.right,array)
            array.append(tree.value)
        return array
test_tree = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
    .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
    .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
    .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)
array=[]
print(preorder(test_tree,array))
print(inorder(test_tree, array))
print(postorder(test_tree, array))