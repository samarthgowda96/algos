class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
       
        return self.leafs(root1) == self.leafs(root2)
        
    def leafs(self, root):
        if not root: return 
        stack = [root]

        leaf =[]
        while stack:
            currentNode = stack.pop()
            print(currentNode)
            if not currentNode:
                print('here')
                continue
            stack.append(currentNode.right)
            stack.append(currentNode.left)            
    
            if currentNode.left is None and currentNode.right is None:
                leaf.append(currentNode.val)
                
        return leaf



 
