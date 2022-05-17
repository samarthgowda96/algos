import csv

# Lists to store your csv columns
A = [] 
B = []

with open('health.csv') as f:  #read your csv
    reader = csv.reader(f, delimiter=',')

    for row in reader: #appending the values
      
        if row:
            if row[0].isdigit(): 
                A.append(int(row[0]))

            if row[1].isdigit():
                B.append(int(row[1]))




n = len(A) + 2 #n to calculate actual sum


def findMissing(A,B,n): 
    
    a_sum, b_sum = sum(A), sum(B) # O(2n)
    actual_sum = n*(n+1)//2 # O(n)

    b_missing = actual_sum - b_sum 

    # Result 1 - integer that exists in B but not in A , // Part A
    ret1 = actual_sum - a_sum - b_missing

    # Result2 - integer that is missing from both A and B, // Part B
    ret2 = b_missing
    
    
    return ret1,ret2

print(findMissing(A,B,n))

# Part C
""" Yes, Part B is already been executed with the following:
1) space complexity: O(1) as the the function uses variables to store the sum of 2 columns and they are independent of size of 2 columns.
2) time complexity : O(N), is  when calculating the actual sum of 2 columns. """