class Solution:
    #Solution 1: Sorting then check consecutive elements
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = sorted(set(nums))
        lastNum = nums[0]
        curLength = 1
        res = 1
        
        for i in range(1, len(nums)):
            if nums[i] == lastNum + 1:
                curLength += 1
            else:
                curLength = 1
            res = max(res, curLength)
            lastNum = nums[i]
            
        return res
    
    #Complexity:
    #Time: O(NlogN), where N is length of nums array
    #Space: O(N)
    
    
    #Solution 2: Top down DP:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        
        @lru_cache(None)
        def dp(num):
            if num not in myset:
                return 0
            
            return dp(num-1) + 1
        
        ans = 0
        for num in nums:
            ans = max(ans, dp(num))
        return ans
    
    #Complexity:
    #Time: O(N), where N is length of nums array
    #Space: O(N)
    
    
    #Solution 3: Find the left most of the consecutive subsequence then expand the right side
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:  # then num is the left most of the consecutive sequence
                left = num
                right = num
                while right + 1 in nums:  # scan to find the right most of the consecutive sequence
                    right += 1
                res = max(res, right - left + 1)
        return res
    
    #Complexity:
    #Time: O(N), where N is length of nums array
    #Space: O(N)
        
