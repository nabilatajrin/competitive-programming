class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #test
        print(len(nums)) #number of digits
        print(len(set(nums))) #types of digits
        
        return len(nums) != len(set(nums))
