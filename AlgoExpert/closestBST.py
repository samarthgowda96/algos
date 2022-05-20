def findClosestValueInBst(tree, target):

    # Write your code here.
	closest = float('inf')
    # Write your code here.
	if tree is None:
		temp = abs(tree.value - target)
        if temp < closest:
            closest = temp
        return closest

    while tree != None:
        temp = abs(tree.value - target)
        if temp < closest: closest = temp #still need to fix the closest value 
        if tree.left != None:
            self.findClosestValueInBst(tree.left, target)
        else:
            self.findClosestValueInBst(tree.right, target)
        
    return closest





