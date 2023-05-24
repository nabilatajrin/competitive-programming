from collections import Counter

class Solution:
    #Simple Python sliding window solution
    def minWindow(self, s: str, t: str) -> str:
        '''
        Keep t_counter of char counts in t
        
        We make a sliding window across s, tracking the char counts in s_counter
        We keep track of matches, the number of chars with matching counts in s_counter and t_counter
        Increment or decrement matches based on how the sliding window changes
        When matches == len(t_counter.keys()), we have a valid window. Update the answer accordingly
        
        How we slide the window:
        Extend when matches < chars, because we can only get a valid window by adding more.
        Contract when matches == chars, because we could possibly do better than the current window.
        
        How we update matches:
        This only applies if t_counter[x] > 0.
        If s_counter[x] is increased to match t_counter[x], matches += 1
        If s_counter[x] is increased to be more than t_counter[x], do nothing
        If s_counter[x] is decreased to be t_counter[x] - 1, matches -= 1
        If s_counter[x] is decreased to be less than t_counter[x] - 1, do nothing
        
        Analysis:
        O(s + t) time: O(t) to build t_counter, then O(s) to move our sliding window across s. Each index is only visited twice.
        O(s + t) space: O(t) space for t_counter and O(s) space for s_counter
        '''
        
        if not s or not t or len(s) < len(t):
            return ''
        t_counter = Counter(t)
        chars = len(t_counter.keys())
        s_counter = Counter()
        matches = 0
        answer = ''
        i = 0
        j = -1 # make j = -1 to start, so we can move it forward and put s[0] in s_counter in the extend phase 
        
        while i < len(s):
            # extend
            if matches < chars: 
                # since we don't have enough matches and j is at the end of the string, we have no way to increase matches
                if j == len(s) - 1:
                    return answer
                j += 1
                s_counter[s[j]] += 1
                if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]:
                    matches += 1

            # contract
            else:
                s_counter[s[i]] -= 1
                if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                    matches -= 1
                i += 1
                
            # update answer
            if matches == chars:
                if not answer:
                    answer = s[i:j+1]
                elif (j - i + 1) < len(answer):
                    answer = s[i:j+1]
        return answer
