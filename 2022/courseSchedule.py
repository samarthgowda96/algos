def traverse(graph, vertex, path, order, visited):
    
    path.append(vertex)
    for nearest in graph[vertex]:
        if nearest not in visited:
            visited.add(nearest)
            traverse(graph, nearest, path, order, visited)
    order.append(path.pop())

def courseSchedule(graph):
    path =[]
    order = []
    visited = set()
    for i in graph:
        if i not in visited:
        traverse(graph, i, path, order, visited)
    print(order)

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

courseSchedule(graph)