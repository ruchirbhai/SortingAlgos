# Given a list of non negative integers, arrange them such that they form the largest number.
# For example:
# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.
A = [30,9, 3, 5, 34]
# class Solution:
    # @param A : tuple of integers
    # @return a strings
    # def largestNumber(self, A):
    #     a = {}
    #     for i in A:
    #         a[i] = []
    #         digits = [int(x) for x in str(i)]
    #         a[i].append(digits)
        
    #     return
    # def largestNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: str
    #     """

    #     # approach: use customized comparator of sorting

    #     class Predicate(str):
    #         def __lt__(self, other):
    #             return self + other < other + self

    #         def __str__()

    #     strs = ''.join(sorted(map(str, nums), key=Predicate, reverse=True))
    #     return '0' if strs[0] == '0' else strs

class LargerNumKey(str):
    def __lt__(x, y):
        print(x,y)
        print(x+y > y+x)
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        # A = [30,9, 3, 5, 34]
        print(sorted(map(str, nums), key=LargerNumKey))
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
if __name__ == "__main__":
    obj = Solution()
    print(obj.largestNumber(A))