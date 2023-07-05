class Solution:
    def combinationSum4(self, nums, target, memo=collections.defaultdict(int)):
        if target < 0: return 0
        if target not in memo:
            memo[target] += sum((1, self.combinationSum4(nums, target - num))[target != num] 
                                for num in nums)
        return memo[target]
    #This is a recursive Python code
    def combinationSum4WithLength(self, nums, target, length, memo=collections.defaultdict(int)):
        if length <= 0: return 0
        if length == 1: return 1 * (target in nums)
        if (target, length) not in memo: 
            for num in nums:
                memo[target, length] += self.combinationSum4(nums, target - num, length - 1)
        return memo[target, length]
