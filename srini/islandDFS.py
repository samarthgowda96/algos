class Graph:
    def __init__(self,row, col,g):
        self.col=col 
        self.row= row
        self.graph=g


    def isSafe(self, i, j, visited):
        return(i>=0 and i<self.row and
               j>=0 and j<self.col and not visited[i][j] and self.graph[i][j])
        
    def DFS(self, i, j, visited):
        rowTemp=[-1,-1,-1,0,0,1,1,1]
        colTemp=[-1,0,1,-1,1,-1,0,1]
        
        visited[i][j]= True
        visit=[]
        lar=0
        for k in range(8):
            if self.isSafe(i+rowTemp[k],j+colTemp[k],visited):
                self.DFS(i+rowTemp[k],j+colTemp[k],visited)
                if self.graph[i+rowTemp[k]][j+colTemp[k]]==1:
                    lar+=1
            visit.append(lar)
        

        print(visit)
            
                




    def countIslands(self):
        print(self.row, self.col)
        visited = []
        for i in range(self.row):
            visited_r = []
            for j in range(self.col):
                visited_r.append(False)
            visited.append(visited_r)
  
        # visited = [[False for j in range(self.col)]for i in range(self.row)]
        count=0
        for i in range(self.row):
            
            for j in range(self.col):
                if visited[i][j]==False and self.graph[i][j]==1:
                    count+=1
                    self.DFS(i, j, visited)

        return count

g=[[0 ,1, 1, 0],
    [ 0, 0 ,0, 0],
    [ 0, 1, 1, 0],
    [0, 1 ,1 ,1]]

""" g = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]] """
row= len(g)
col= len(g[1])

graph= Graph(row, col, g) 
print("No of tiny islands in the this tiny world are:",graph.countIslands())

