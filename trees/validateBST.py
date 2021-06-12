class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left= None
    
    def insert(self,value):
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
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode= currentNode.right
        return self

def validate(tree):
    return validate_helper(tree, float("-inf"), float("-inf"))
def validate_helper(tree, minn, maxx):
    if tree is None or tree.value is None:
        return True


    if tree.value >= minn or tree.value < maxx:
        return True
    else:

        return False
    
    if tree.left is None:
        left_is_valid= True
    else:
        left_is_valid= validate_helper(tree.left, minn, tree.value)

    if tree.right is None:
        right_is_valid = True
    else:
        right_is_valid= validate_helper(tree.right,tree.value,maxx)

    return left_is_valid and right_is_valid
test_tree = BST(100).insert(-150).insert(15).insert(5).insert(2).insert(1).insert(22) \
    .insert(1).insert(1).insert(-3).insert(1).insert(1).insert(502).insert(55000) \
    .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
    .insert(-51).insert(-403).insert(1001).insert(-57).insert(60).insert(4500)
    
isvalid= validate(test_tree)
print(isvalid)

