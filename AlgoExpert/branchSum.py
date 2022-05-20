# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	totalSum = []
	leftSum  = 0
	rightSum = 0
	return total(root, totalSum, leftSum)
	
    # Write your code here.
def total(root, totalSum, leftSum):
	if root is None:
		return root
	leftSum += root.value 
	if root.left is None and root.right is None:
		totalSum.append(leftSum)
	total(root.left, totalSum, leftSum)
	total(root.right, totalSum, leftSum)
		
	return totalSum