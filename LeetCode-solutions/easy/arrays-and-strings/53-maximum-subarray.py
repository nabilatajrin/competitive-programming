#LeetCode: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
-----------------------
Here's a Python solution to solve this problem using Kadane's algorithm:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max_sum with the first element of the array
        current_sum = nums[0]  # Initialize current_sum with the first element

        for i in range(1, len(nums)):
            # Update the current_sum to either the current element or the sum of the current element and the previous current_sum
            current_sum = max(nums[i], current_sum + nums[i])
            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum
