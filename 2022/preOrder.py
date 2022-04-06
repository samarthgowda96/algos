# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited =[]
        if root:
            self.travelTheWorldSoon(root, visited)
        return visited
    
    def travelTheWorldSoon(self, root, visited):
            visited.append(root.val)
            if root.left is not None :
                self.travelTheWorldSoon(root.left, visited)
            if root.right is not None :
                self.travelTheWorldSoon(root.right, visited)