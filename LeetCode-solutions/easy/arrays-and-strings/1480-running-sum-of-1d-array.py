class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        print(nums)
        for i in range(1, len(nums)):
            print(nums[i])
            print(nums[i-1])
            nums[i] += nums[i-1]
            print('sum:',nums[i])
        return nums
