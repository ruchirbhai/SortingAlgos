# Problem Description
# Given an integer array A of size N.
# You can pick B elements from either left or right end of the array A to get maximum sum.
# Find and return this maximum possible sum.
# NOTE: Suppose B = 4 and array A contains 10 elements then:
# You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . 
# you need to return the maximum possible sum of elements you can pick.
# Problem Constraints
# 1 <= N <= 105
# 1 <= B <= N
# -10^3 <= A[i] <= 10^3
# Input Format
# First argument is an integer array A.
# Second argument is an integer B.
# Output Format
# Return an integer denoting the maximum possible sum of elements you picked.
# Example Input
# Input 1:
#  A = [5, -2, 3 , 1, 2]
#  B = 3
# Input 2:
#  A = [1, 2]
#  B = 1
# Example Output
# Output 1: 8
# Output 2: 2

# Example Explanation
# Explanation 1:
#  Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
# Explanation 2:
#  Pick element 2 from end as this is the maximum we can get

# HINT-------------------------------------------------------------
# Maintain two arrays prefix[i] and suffix[i] where prefix[i] denotes sum of elements 
# from index [0,i] and suffix[i] denotes sum of elements from index [i,N-1].
# Now iterate from left and one by one pick elements from left for example: 
# if you pick ‘a’ elements from left and remaining ‘k-a’ elements from right.
# So the sum in this case will be prefix[a-1] + suffix[n-(k-a)]
# Maintain the maximum among all and return it.
# Time Complexity: O(N)
# Space Complexity: O(N)
# where N is number of elements in array A

# import sys
A = [5, -2, 3 , 1, 2]
B = 3

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        left_sum =[0] * (B + 1)
        right_sum = [0] * (B + 1)
        length = len(A) - 1
        for i in range(B):
            left_sum[i+1] = left_sum[i] + A[i]
            right_sum[i+1] = right_sum[i] + A[length-i]
        # initialize max_val to lowest -ve value!! keep in mind!!
        max_val = float('-inf')
        for i in range(B):
            val = left_sum[i] + right_sum[B-i]
            max_val = int(max(max_val,val))
        return max_val

    def solve_brute2(self, A, B):
        left_ptr = 0
        max_sum = int()
        while left_ptr <= B:
            right_val = int()
            
            right_ptr = len(A) - 1
            if left_ptr == 0:
                for i in range(B):
                    right_val += A[right_ptr-i]
                left_val = A[left_ptr]
                left_ptr += 1
                max_sum = right_val
            else:
                right_val = int()
                for j in range(B-left_ptr):
                    right_val += A[right_ptr]
                    right_ptr -= 1
                max_sum = max(max_sum,(left_val+right_val))
                left_val += A[left_ptr]
                left_ptr += 1
                
        return max_sum

    def solve_brute(self, A, B):
        left_ptr = 0
        max_sum = int()
        # for i in range(B):
        #     while 

        while left_ptr <= B:
            right_val = int()
            left_val = int()
            right_ptr = len(A) - 1
            if left_ptr == 0:
                for i in range(B):
                    right_val += A[right_ptr-i]
                left_ptr += 1
                max_sum = right_val
            else:
                for i in range(left_ptr):
                    left_val += A[i]
                    # left_ptr +=1
                
                right_val = int()
                for j in range(B-left_ptr):
                    right_val += A[right_ptr]
                    right_ptr -= 1
                    # max_sum = max(max_sum,(left_val+right_val))
                    # left_ptr += 1
                max_sum = max(max_sum,(left_val+right_val))
                left_ptr += 1
        return max_sum
if __name__ == "__main__":
    aux = Solution()
    # aux =findZeroSum(arr["data"+str(i+1)])
    print(aux.solve(A,B))