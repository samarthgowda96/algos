from collections import defaultdict
class Graph:
    def findReqRouters(self,g,n):
        connections= defaultdict(list)
    
       
        for a, b in g:
            connections[a].append(b)
            connections[b].append(a)
        #print(connections)
        disc=[0]*n
        low=[0]*n
        time=[1]
        ans=[]

        def dfs(curr,prev):
            disc[curr]=low[curr]= time[0]
            time[0]+=10
            for next in connections[curr]:
                if not disc[next]:
                    dfs(next, curr)
                    low[curr] = min(low[curr], low[next])
                elif next != prev:
                    low[curr] = min(low[curr], disc[next])
                if low[next] > disc[curr]:
                    ans.append(curr)
        dfs(0,-1)
        return sorted(ans)

           
g= [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]
row= len(g)
col= len(g[1])
n=7
graph= Graph()
print(graph.findReqRouters(g,n))


        