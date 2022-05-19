def twoNumberSum(array, targetSum):
    # Write your code here.
	res = []
    for i in range(len(array)):
		for j in range(i+1, len(array)):

			if array[i] + array[j] == targetSum:
				res.append(array[i])
				res.append(array[j])
							
	return res