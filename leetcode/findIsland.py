class GRAPH:
    def __init__(self,g,col,row):
        self.row= row
        self.col= col
        self.graph=g
    
    def findIsland(self):
        count=0
        if not self.graph:
            return 0
        for i in range(self.row):
            for j in range(self.col):
                if self.graph[i][j]!="1":
                    continue
                else:
                    print(self.graph[i][j])
                
        return count

    def dfs(self,graph,i,j):
        if i<0 or j<0 or i>=self.col or i>= self.row or self.graph[i][j]!='1':
            return
        self.graph[i][j]="0"
        self.dfs(self.graph,i+1,j)
        self.dfs(self.graph,i-1,j)
        self.dfs(self.graph,i,j+1)
        self.dfs(self.graph,i,j-1)


g=[[1 ,1, 1, 0],
    [ 1, 0 ,0, 0],
    [ 0, 1, 1, 0],
    [0, 1 ,1 ,1]]


row= len(g)
col= len(g[1])


graph= GRAPH(g,col,row)
print(graph.findIsland())

