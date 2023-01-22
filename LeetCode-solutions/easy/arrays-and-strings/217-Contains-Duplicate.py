LeetCode: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #test
        print(len(nums)) #total number of digits
        print(len(set(nums))) #number of unique digits
        return len(nums) != len(set(nums))
    
    
Solution 2:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
