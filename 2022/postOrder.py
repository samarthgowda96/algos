class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited =[]
        if root:
            self.travelTheWorldSoon(root, visited)
        return visited
    
    def travelTheWorldSoon(self, root, visited):
            print(root)
            if root.left is not None :
                self.travelTheWorldSoon(root.left, visited)
            if root.right is not None :
                self.travelTheWorldSoon(root.right, visited)
            visited.append(root.val)
           
       