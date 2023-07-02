class Solution:
    #Complexity: time complexity is O(n), because we use dp problem with complexity O(n) twice. Space complexity is O(1), because in python lists passed by reference and space complexity of House Robber problem is O(1).
    def rob(self, nums):
        def rob_helper(nums):
            dp1, dp2 = 0, 0
            for num in nums:
                dp1, dp2 = dp2, max(dp1 + num, dp2)          
            return dp2
        return max(nums[0] + rob_helper(nums[2:-1]), rob_helper(nums[1:]))
