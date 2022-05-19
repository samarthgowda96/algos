def sortedSquaredArray(array):
    # Write your code here
	
	for i in range(len(array)):
		temp = array[i] * array[i]
		array[i] = temp 
    return sorted(array) 
