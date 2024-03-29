#LeetCode: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p) #The append() method in python adds a single item to the existing list.
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
