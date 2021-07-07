def validSq(root,arr):
    if root is None: return None
    l=len(arr)
    res=self.ishelper(root,l,i,arr)
    return res 

def ishelper(root,l,i,arr):
    
    if root.val != arr[0] :
        return False
    if (i==l-1) and root.left==None and root.right==None and root.val==arr[i]:
        return True
    if i<l and root.val==arr[i]:
        return self.ishelper(root.left,l,i+1,arr) or self.ishelper(root.right,i+1,arr)

   
    