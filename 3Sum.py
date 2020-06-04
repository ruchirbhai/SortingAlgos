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
# data = [-6, -4, 1, 3, 9, 10]
# data = [5,-2,2,0,-1,1]
# data = [6, 0, 0, 0, 0, 0, 0]
data = [6,10,3,-4,1,-6,9]

def findZeroSum_bruteforce(arr):
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

def findZeroSum(arr):
    arr.sort()
    triplet = []
    length = len(arr)
    # print(arr)
    for num1 in range(length-2):
        if (num1 == 0 or arr[num1] != arr[num1-1]) and arr[num1] <= 0:
            left= num1 +1 #left pointer
            right = length - 1 # right pointer
            while left < right:
                sum = arr[left] + arr[right] + arr[num1] 
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                elif sum == 0:
                    triplet.append(f"{arr[num1]},{arr[left]},{arr[right]}")
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1

    for data in triplet:
        print(data)
    return triplet

# findZeroSum_bruteforce(data)
findZeroSum(data)
