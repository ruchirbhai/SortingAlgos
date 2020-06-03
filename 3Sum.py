# 3 Sum
# Given an integer array arr of size n, find all magic triplets in it.
# Magic triplet is a group of three numbers whose sum is zero.
# Note that magic triplets may or may not be made of consecutive numbers in arr.
# Example One
# Input: arr = [10, 3, -4, 1, -6, 9] Output: [“10,-4,-6”, “3,-4,1”]
# Example Two
# Input: arr = [12, 34, -46]  Output: [“12,-46,34”]
# Example Three
# Input: arr = [0, 0, 0];  Output: [“0,0,0”]
# Example Four
# Input: arr = [-2, 2, 0 -2, 2]; Output: [“2,-2,0”]
# Notes
# Input Parameters: Function has one argument: array of integers arr.
# Output: Function must return an array of strings. Each string (if any) in the array must represent a unique magic triplet and strictly follow this format: “1,2,-3” (no whitespace, one comma between numbers).
# Order of the strings in the array is insignificant. Order of the integers in any string is also insignificant. For example, if [“1,2,-3”, “1,-1,0”] is a correct answer, then [“0,1,-1”, “1,-3,2”] is also a correct answer.
# Triplets that only differ by order of numbers are considered duplicates, and duplicates must not be returned. For example, if “1,2,-3” is a part of an answer, then “1,-3,2”, “-3,2,1” or any permutation of the same numbers may not appear in the same answer (though any one of them may appear instead of “1,2,-3”).
# Constraints:
# 1 <= n <= 2000
# -1000 <= any element of arr <= 1000
# arr may contain duplicate numbers.
# arr is not necessarily sorted.

#try 1 brute Force method
data = [-6, -4, 1, 3, 9, 10]
def findZeroSum(arr):
    arr.sort()
    triplet_set = set()
    # print(arr)
    for i in range(len(arr)-1):
        num1 = arr[i]
        for j in range((len(arr)-i-1)):
            num2 = arr[j+i+1]
            for k in range((len(arr)-i-j-1)):
                if (k+j+i+2) <= (len(arr) -1):
                    num3 = arr[k+j+i+2]
                    if num1 + num2 + num3 == 0:
                        data = str(num1) + "," + str(num2) + "," + str(num3)
                        # print(data)
                        triplet_set.add(data)
                        break
    for triplet in triplet_set:
        print(triplet)
    return triplet_set

findZeroSum(data)
