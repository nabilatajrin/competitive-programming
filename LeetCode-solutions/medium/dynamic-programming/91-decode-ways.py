class Solution:
    #bottom up dynamic programming:
    #index 0: extra base offset. dp[0] = 1
    #index 1: # of ways to parse "2" => dp[1] = 1
    #index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
    #index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1)

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        return dp[len(s)]
