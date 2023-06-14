class Solution:
    #sort and dictionary
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
    def isAnagram2(self, s, t):
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2
    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)
    
---------------------    
Efficient Solution 2:
    Use:
        -hashmap
        -loop and conditions
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
--------------------- 
Efficient solution using py library:
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            return Counter(s) == Counter(t)
        
--------------------- 
Less efficient solution using py library:
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            return sorted(s) == sorted(t)
