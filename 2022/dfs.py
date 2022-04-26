class Solution:
    

    def dfs(self, graph, stack):
        if graph is None:
            return 0
        if graph.left is not None  or graph.right is not None:
            return max(dfs(graph.left), dfs(graph.right)) +1
        else:
            return min(dfs(graph.left), dfs(graph.right)) +1
        
        
        
           

                












graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
sol = Solution()
print(sol.traverse(graph))
