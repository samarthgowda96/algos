def isValidSubsequence(array, sequence):
	i = 0 #array
	j = 0 #seq
    # Write your code here.
	res = []
	while i < len(array) and j < len(sequence):
		if array[i] == sequence[j]:
			print(array[i], sequence[j])
			res.append(array[i])
			i += 1
			j += 1
		else:
			i += 1
			
	#print(res,"--", sequence)
	return res == sequence 