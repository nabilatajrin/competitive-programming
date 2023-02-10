class Solution:
    #Simple Python two-pointer solution
    
    def characterReplacement(self, s, k):        
        longest_window = 0
        window_counts = collections.defaultdict(int)
        l = 0
        
        for r in range(len(s)):
            window_counts[s[r]] += 1
            while r - l + 1 - max(window_counts.values()) > k:
                window_counts[s[l]] -= 1 
                l += 1
            longest_window = max(longest_window, r - l + 1)
        return longest_window
