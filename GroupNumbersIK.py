# Group the numbers
# You are given an integer array arr of size n. Group and rearrange them (in-place) 
# into evens and odds in such a way that group of all even integers appears on the 
# left side and group of all odd integers appears on the right side. 
# Example

# Input: [1, 2, 3, 4]
# Output: [4, 2, 1, 3]
# Order does not matter. Other valid solutions are: 
# [2, 4, 1, 3]
# [2, 4, 3, 1]
# [4, 2, 3, 1]

import time
arr = {
    "data1" : [5,4,1,3,2],      # happy path easy to vizualize
    "data2" : [5,4,1999,3,2,8,7,6,10,100],     #larger range of values
    "data3" : [5,4,1,3,2,2],        # repeated values
    "data4" : [1,1,1,1,1,1],        # every element is the same
    "data5" : [0,22,100,1,2,3,4,5,6,7,7,8,89,9,0,-1],   #negative + zero
    "data6" : [5,4,3,2,1],      #reverse sorted array
    "data7" : [1],      # data with only 1 value
    "data8" : [],       # data with  NULL value
    "data9" : [1,1]     #failed on IK for some reason
}


def solve(arr):
    length = len(arr)
    
    if length <=1:
        return arr
    
    left_ptr, right_ptr = 0, length - 1
    curr_ptr = 0
    
    while left_ptr <= right_ptr:
        if (arr[curr_ptr]%2) == 0:
            arr[curr_ptr],arr[left_ptr] = arr[left_ptr],arr[curr_ptr]
            left_ptr += 1
            curr_ptr +=1
        else: # value is odd
            arr[curr_ptr], arr[right_ptr] = arr[right_ptr],arr[curr_ptr]
            right_ptr -= 1
            # Remeber to NOT increment the curr_ptr when swapping on the right side!! 
            # As the right side values are not yet tested for odd/even cases
            # curr_ptr +=1
    return arr

if __name__ == "__main__":
    # Call the dataset to test Bubble sort
    for i in range(len(arr)):
        start_time = time.time()
        aux = solve(arr["data"+str(i+1)])
        print(aux)
        print("Merge time for data" + str(i+1) + " = "+ str(time.time() - start_time))