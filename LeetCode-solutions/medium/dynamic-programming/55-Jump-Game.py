class Solution:
    #Solution 1: Top down DP (Sometime TLE):
    #Let dp(i) denote the possibility if we can reach the last index if we are at index i.
    #Then dp(0) is our result.
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return True
            
            for j in range(i+1, min(i+nums[i], n-1) + 1):
                if dp(j):
                    return True
            return False
        
        return dp(0)
    
    #Complexity:
    #Time: O(N^2), where N <= 10^4 is length of nums array.
    #Space: O(N)
    
    
    #Solution 2: Top down DP:
    #Let dp[i] denote the possibility if we can reach the last index if we are at index i.
    #Then dp[0] is our result.
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            for j in range(i+1, min(n, i+nums[i]+1)):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
    
    #Complexity:
    #Time: O(N^2), where N <= 10^4 is length of nums array.
    #Space: O(N)
    
    
    #Solution 3: Max Pos So Far:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxPos = 0
        i = 0
        while i <= maxPos:
            maxPos = max(maxPos, i + nums[i])
            if maxPos >= n - 1: return True
            i += 1
        
        return False
    
    #Complexity:
    #Time: O(N), where N <= 10^4 is length of nums array.
    #Space: O(1)
