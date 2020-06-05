# arr = [[1, 3, 5, 7], [2, 4, 6, 8],[0, 9, 10, 11]]
# N = len(arr[0])

# def mergeArrays(arr):
#     #
#     # Write your code here.
#     #row of the 2D array is k i.e. number of arrays
#     K = len(arr)
#     # length of the each array is the coloum length
#     final = [0] *(K*N)
#     # helper arguments are (array, start,end, length of array?)
#     merge_helper(arr,0,K-1,final)
    
#     return final

# def merge_helper(data, start, end, final):
#     # DIVIDE Part 
#     if start == end:
#         for i in range(N):
#             val = start * N + i
#             final[val] = data[start][i]
#         return 
#     mid = (start+end)//2
#     aux = []
#     #left side of the array i.e the top half in this case
#     merge_helper(arr, 0, mid, final)
#     # call the bottom half
#     merge_helper(arr, mid+1, end,final)
    
#     # now time to MERGE
#     i = start
#     j = start
    
#     while i <= N -1 and j <= N-1:
#         if data[start][i] <= data[end][j]:
#             aux.append(data[start][i])
#             i += 1
#         else:
#             aux.append(data[end][j])
#             j += 1
    
#     while i <= N-1:
#         aux.append(data[start][i])
#         i+=1
#     while j <=N-1:
#         aux.append(data[end][j])
#         j+=1
#     print(aux)
#     # final[0:len(aux)+1] =aux
#     aux_length= len(aux)
#     final_length = len(final)


#     return final

# mergeArrays(arr)

# Python3 program to merge K sorted arrays 
n = 4 ; 

# Function to perform merge operation 
def merge(l, r, output) : 
	
	# to store the starting point of 
	# left and right array 
	l_in = l * n ; 
	r_in = ((l + r) // 2 + 1) * n; 

	# to store the size of left and 
	# right array 
	l_c = ((l + r) // 2 - l + 1) * n; 
	r_c = (r - (l + r) // 2) * n; 

	# array to temporarily store left 
	# and right array 
	l_arr = [0] * l_c; r_arr = [0] * r_c; 

	# storing data in left array 
	for i in range(l_c) : 
		l_arr[i] = output[l_in + i]; 

	# storing data in right array 
	for i in range(r_c) : 
		r_arr[i] = output[r_in + i]; 

	# to store the current index of 
	# temporary left and right array 
	l_curr = 0 ; r_curr = 0; 

	# to store the current index 
	# for output array 
	in1 = l_in; 

	# two pointer merge for two sorted arrays 
	while (l_curr + r_curr < l_c + r_c) : 
		if (r_curr == r_c or (l_curr != l_c and
			l_arr[l_curr] < r_arr[r_curr])) : 
			output[in1] = l_arr[l_curr]; 
			l_curr += 1; in1 += 1; 
		else : 
			output[in1] = r_arr[r_curr]; 
			r_curr += 1; in1 += 1; 

# Code to drive merge-sort and 
# create recursion tree 
def divide(l, r, output, arr) : 
	
	if (l == r) : 

		# base step to initialize the output 
		# array before performing merge 
		# operation 
		for i in range(n) : 
			output[l * n + i] = arr[l][i]; 

		return; 
	
	# to sort left half 
	divide(l, (l + r) // 2, output, arr); 

	# to sort right half 
	divide((l + r) // 2 + 1, r, output, arr); 

	# merge the left and right half 
	merge(l, r, output); 

# Driver code 
if __name__ == "__main__" : 

	# input 2D-array 
	arr = [[1, 3, 5, 7], [2, 4, 6, 8],[0, 9, 10, 11]];
	
	# Number of arrays 
	k = len(arr); 
	
	# Output array 
	output = [0] * (n * k); 
	
	divide(0, k - 1, output, arr); 
	
	# Print merged array 
	for i in range(n * k) : 
		print(output[i], end = " "); 

# This code is contributed by Ryuga 
