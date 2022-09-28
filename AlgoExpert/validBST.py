# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# INORDER TRAVERSAL IS ALWAYS ASC IF TREE IS A BST
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = []
        res = self.inorder(root, stack)
        if len(res) != len(set(res)):
            return False
        return res == sorted(res)
        
    
     def inorder(self, root, stack):
        if root is None:
            return 
        self.inorder(root.left, stack)
        stack.append(root.val)
        self.inorder(root.right, stack)
        return stack 
        
        