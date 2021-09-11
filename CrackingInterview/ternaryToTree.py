""" class Node:
    def __init__(self,val):
        self.val=val
        self.right= None
        self.left= None
   

    def insert(self,exp):
        stack=[]
        temp=Node(None)
        stack.append(temp)
        res=[]
        for i in range(len(exp)):
            c= exp[i]
            if(c=="?"):
                stack[0].left= Node(None)
                stack.append(stack[0].left)
            elif(c==":"):
                stack.pop()
                stack[0].right= Node(None)
                stack.append(stack[0].right)
            else:
                stack[0].val= c
                res.append(c)
       

        return res

     
        

exp="b?a:e?d:a"

N = Node(None)
print(N.insert(exp))

 """
class Node:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self):
        curLevel = [self]
        nextLevel = []
        ans = []
        while curLevel:    
            curAns = []
            for x in curLevel:
                curAns.append(x.val)
                if x.left: nextLevel.append(x.left)
                if x.right: nextLevel.append(x.right)
            ans.append(curAns)
            curLevel = nextLevel
            nextLevel = []
        return ans

class Solution:
    
    def toTree(self, s):
        if not s: return None
        
        root = Node(s[0])
        stack = [root]
        for i in range(1, len(s)-1, 2):
            node = Node(s[i+1])
            if s[i] == '?': stack[-1].left = node
            elif s[i] == ':':
                stack.pop()
                while stack[-1].right: stack.pop()
                stack[-1].right = node
            stack.append(node)
        print(root.levelOrder())
        return root
        
s = Solution()
s.toTree("a?b:c") # [['a'], ['b', 'c']]
s.toTree("a?b?c:d:e") # [['a'], ['b', 'e'], ['c', 'd']]
s.toTree("a?b:c?d:e") # [['a'], ['b', 'c'], ['d', 'e']]
