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
def largestValues(tree):
    largestVals=[]
    dfs(tree,largestVals,0)
    return largestVals

def dfs(tree, largestVals, level):
    if tree is None:return

    if (level==len(largestVals)):
        largestVals.append(tree.value)

    else:
        largestVals[level]= max(largestVals[level],tree.value)

    dfs(tree.left, largestVals, level+1)
    dfs(tree.right, largestVals,level+1) 

tree= BST(10).insert(2).insert(3).insert(1).insert(100)
print(largestValues(tree))



