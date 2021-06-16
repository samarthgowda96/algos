from collections import deque 
class Graph:
    def __init__(self,row, col,g):
        self.row= row
        self.col= col
        self.graph= g

    def findTreasue(self):
        q= deque([((0,0),0)])
        print(q)
        self.graph[0][0]="D" 
        if self.col== 0 or self.row==0:
            return -1 #impossible
        
        while q:
            (x,y),step= q.popleft()
           
            for i , j in [[0,1],[0,-1], [1,0],[-1,0]]:   # CHECKING BFS LOOP
                if 0<= i+x <self.row and 0<= j+y < self.col:
                    if self.graph[i+x][j+y]=="X":
                        return step+1
                        
                    elif self.graph[i+x][j+y]=="O":
                        self.graph[i+x][j+y]="D"
                        q.append(((i+x,j+y),step+1))
            (x,y),step= q.popleft()
            print((x,y),step)
                        
        return q

                
        

g=[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]
row= len(g)
col= len(g[1])
graph= Graph(row, col, g) 
print(graph.findTreasue())

