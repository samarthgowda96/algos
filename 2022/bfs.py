class Node:
    def __init__(self, name):
        self.name  = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))

    def bfs(self):
        queue = [self]
        array = []
        while len(queue) > 0:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for i in currentNode.children:
                queue.append(i)
        return array

node = Node("A")
node.addChild("M")

node.addChild("M")
node.addChild("Y")

print(node.bfs())

