def areSymmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (roo1 is None)) or root1.val != root2.val:
        return False
    else:
        return areSymmetric(root1.left, root2.right) and areSymmetric(root1.right, root2.left)


def isSymmetric(root):
    if root is None: return True
    return areSymmetric(root.left, root.right) 
        
        