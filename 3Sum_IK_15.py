# https://leetcode.com/problems/3sum/
# 3 Sum
# Given an integer array arr of size n, find all magic triplets in it.
# Magic triplet is a group of three numbers whose sum is zero.
# Note that magic triplets may or may not be made of consecutive numbers in arr.
# Example One
# Input: arr = [10, 3, -4, 1, -6, 9]
# Output: [“10,-4,-6”, “3,-4,1”]
# Example Two
# Input: arr = [12, 34, -46]
# Output: [“12,-46,34”]
# Example Three
# Input: arr = [0, 0, 0];
# Output: [“0,0,0”]
# Example Four
# Input: arr = [-2, 2, 0 -2, 2];
# Output: [“2,-2,0”]
# Notes
# Input Parameters: Function has one argument: array of integers arr.


import time
arr = {
    "data1" : [0,0,0],      # happy path easy to vizualize
    "data2" : [-1,0,1,2,-1,-4],     #larger range of values
    "data3" : [5,4,1,3,2,2],        # repeated values
    "data4" : [1,1,1,1,1,1],        # every element is the same
    "data5" : [0,22,100,1,2,3,4,5,6,7,7,8,89,9,0,-1],   #negative + zero
    "data6" : [5,4,3,2,1],      #reverse sorted array
    "data7" : [1],      # data with only 1 value
    "data8" : [],       # data with  NULL value
    "data9" : [1,1]     #failed on IK for some reason
}

def findZeroSum(nums):
    # Write your code here.
    # left_ptr, run_ptr = 0, 2
    #sort arr
    nums.sort()
    result = []
    length = len(nums) - 2

    for index in range(length):
        # Here we check for 3 conditions 
        # 1 base case when num1 = 0
        # 2 weed out duplicates in num1 i.e. arr[num1]!=arr[num1-1]
        # 3 Skip all the +ve vlaues for our base case number since the array is sorted their addition will 
        # never result in a output zero IT WILL ALWAYS BE GREATER THAN ZERO
        if (index == 0 or nums[index] != nums[index-1]) and nums[index] <= 0:
            left_ptr = index +1
            right_ptr = length +1   # End of list

            while left_ptr < right_ptr:
                sum = nums[index] + nums[left_ptr] + nums[right_ptr]
                if sum > 0:
                    right_ptr -= 1
                elif sum < 0:
                    left_ptr += 1
                else:   # sum == 0
                    result.append(f"{nums[index]},{nums[left_ptr]},{nums[right_ptr]}")
                    # Increment the pointers
                    left_ptr += 1
                    right_ptr -= 1
                    
                    #Take care od duplicates
                    while nums[left_ptr] == nums[left_ptr-1]:
                        left_ptr += 1
                        
                    while nums[right_ptr] == nums[right_ptr+1]:
                        right_ptr -= 1
        # if (num1 == 0 or arr[num1] != arr[num1-1]) and arr[num1]<= 0:
        #     left = num1 + 1
        #     right = len(arr) -1
            
        #     while left < right:
        #         sum = arr[num1] + arr[left] + arr[right]
        #         if sum > 0:
        #             right -= 1
        #         elif sum < 0:
        #             left += 1
        #         else:
        #             result.append(str(arr[num1]) + "," + str(arr[left]) + "," + str(arr[right]))
        #             # increment the pointers
        #             left += 1
        #             right -= 1
        #             # Take care of the duplicate values in the array for the left_ptr
        #             while left<right and arr[left] == arr[left+1]:
        #                 left +=1
        #             # Take care of the duplicate values in the array for the left_ptr
        #             while left<right and arr[right] == arr[left-1]:
        #                 right -=1

    # This was the first instinct which was not very accurate and messy code too
    # while left_ptr < len(arr) - 2:
    #     if arr[left_ptr] + arr[left_ptr + 1] + arr[run_ptr] > 0:
    #         left_ptr += 1
    #         run_ptr = left_ptr + 2
    #         break
    #     if arr[left_ptr] + arr[left_ptr + 1] + arr[run_ptr] == 0:
    #         result.append(str(arr[left_ptr]) + "," + str(arr[left_ptr + 1]) + "," + str(arr[run_ptr]))
    #         left_ptr += 1
    #         break
    #     elif arr[left_ptr] + arr[left_ptr + 1] + arr[run_ptr] < 0:
    #         while run_ptr <= len(arr)-1:
    #             if arr[left_ptr] + arr[left_ptr + 1] + arr[run_ptr] > 0:
    #                 left_ptr += -1
    #                 run_ptr = left_ptr + 2
    #                 break
    #             if arr[left_ptr] + arr[left_ptr + 1] + arr[run_ptr] == 0:
    #                 result.append(str(arr[left_ptr]) + "," + str(arr[left_ptr + 1]) + "," + str(arr[run_ptr]))
    #                 left_ptr += 1
    #                 break
    #             run_ptr += 1
    #         left_ptr += 1
    #         run_ptr = left_ptr + 2
    
    return result

if __name__ == "__main__":
    # Call the dataset to test Bubble sort
    for i in range(len(arr)):
        start_time = time.time()
        aux = findZeroSum(arr["data"+str(i+1)])
        print(aux)
        print("Merge time for data" + str(i+1) + " = "+ str(time.time() - start_time))