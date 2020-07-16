# Lexicographical Order
# Given a bunch of key-value pairs, for each unique key find 1) the number of values and 
# 2) the lexicographically greatest value.
# Example One
# Input is an array of strings, each with a key and a value separated by a space:
# ["key1 abcd",
#  "key2 zzz",
#  "key1 hello",
#  "key3 world",
#  "key1 hello"]
# Output is an array of strings with unique keys followed by a colon, the total number of 
# values, a comma, and the lexicographically greatest of the values associated with that key in the input:
# ["key1:3,hello",
#  "key2:1,zzz",
#  "key3:1,world"]
# The order or strings in the output is insignificant; these same strings in a different order are also a correct output.
# Example Two
# Input:
# ["mark zuckerberg",
#  "tim cook",
#  "mark twain"]
# Output:
# ["mark:2,zuckerberg",
#  "tim:1,cook"]
# or
# ["tim:1,cook",
#  "mark:2,zuckerberg"]
class Solution:
    def solve(self, arr):
        # traverrse through the array and process it into a dict
        res_d = {}
        for item in arr:
            key,value = item.split()
            if key not in res_d:
                res_d[key] = [1,value]
            else:
                res_d[key][0] += 1
                if res_d[key][1] < value:
                    res_d[key][1] = value
        
        result = []
        for key in res_d:
            result.append(f"{key}:{res_d[key][0]},{res_d[key][1]}")
        return result

if __name__ == "__main__":
    obj = Solution()
    arr = ["key1 abcd","key2 zzz","key1 hello","key3 world","key1 hello"]
    print(obj.solve(arr))