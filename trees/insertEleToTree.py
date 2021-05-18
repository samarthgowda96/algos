from collections import dequeue
class BinaryTree(object):
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right=None
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data

    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def insertLeft(self,newNode):
        if self.left==None:
            self.left= BinaryTree(newNode)
        else:
            temp= BinaryTree(newNode)
            temp.left= self.left
            self.left= temp
    
    def insertRight(self, newNode):
        if self.right==None:
            self.right= BinaryTree(newNode)
        else:
            temp= BinaryTree(newNode)
            temp.right = self.right
            self.right= temp

    def insertInLevOrderTraversal(root,data):
        newNode= BinaryTree(data)
        if root is None:
            root= newNode
            return root
        q= Queue()
        q.append(root)
        node = root
        while not q.isEmpty():
            node = q.deQueue()
            if data == node.getData():
                return root
            if node.left is not None:
                q.enQueue(node.left)
            else:
                node.left= newNode
                return root
            if node.right is not None:
                q.enQueue(node.right)
            else:
                nodde.right= newNode
                return root




tree= BinaryTree(1)
tree.insertLeft(3)
tree.insertRight(5)
tree.insertLeft(2)
tree.insertInLevOrderTraversal(7)
print(tree.getData())
