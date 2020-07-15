# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

import time
arr = {
    "data1" : [2,7,11,15],
}

target = 9

class Solution:
    def twoSum(self, arr, target):
        # Brute force approach require 2 loops. either 2 for loops or 1 for 1 while loop
        # so we can use the hashmap which is the dictionary solution in  python and this will be one pass to
        # our time complexity will be O(n) when using a dictionary to keep track of the values already analyzed
        
        # seen is our dictionary for the values already analyzed
        seen = {}
        
        # start the iteration we use enumerate as that will help us keep track of the index
        # Python program to illustrate 
        # # enumerate function 
        # l1 = ["eat","sleep","repeat"] 
        # # creating enumerate objects 
        # obj1 = enumerate(l1) 
        # print "Return type:",type(obj1) 
        # print list(enumerate(l1)) 
        # Output:
        # Return type: < type 'enumerate' >
        # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
        for index, num in enumerate(arr):
            remainder = target - num
            if remainder in seen:
                return (seen[remainder], index)
            else:
                seen[num] = index

if __name__ == "__main__":
    # Call the dataset to test Bubble sort
    for i in range(len(arr)):
        start_time = time.time()
        aux = Solution()
        # aux =findZeroSum(arr["data"+str(i+1)])
        print(aux.twoSum(arr["data"+str(i+1)],target))
        print("Merge time for data" + str(i+1) + " = "+ str(time.time() - start_time))