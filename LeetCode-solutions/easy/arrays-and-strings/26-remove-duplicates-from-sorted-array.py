LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
 
Constraints:
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.

------------------------------------------------------------------------------------------------------------------------------------------------------
def remove_duplicates(nums):
    """
    Removes the duplicates from a sorted array.
    Args:
        nums: A list of integers.
    Returns:
        The new length of the array.
    """
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1
------------------------------------------------------------------------------------------------------------------------------------------------------------
Solution:

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        return len_

-----------------------------------------
def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Empty array, so no duplicates.

        # Use two pointers: one to iterate the array, and the other to mark the position to    insert unique elements.
        j = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                # Found a new unique element, insert it at the correct position.
                j += 1
                nums[j] = nums[i]

        return j + 1  # Length of the array with unique elements.

Explanation:
The function remove_duplicates takes a sorted list nums as input.

We first check if the list is empty. If it is empty, there are no duplicates, and we return 0 as the length of the modified array.

We use two pointers: i and j. The pointer i iterates through the array starting from index 1, and the pointer j marks the position to insert unique elements.

We loop through the array starting from index 1 (since the first element is always unique).

If the current element nums[i] is different from the element at nums[j], it means we found a new unique element. So, we increment j by 1 and update the value at index j with the unique element at nums[i].

We repeat this process until i reaches the end of the array.

After the loop, j will be the index of the last unique element in the modified array.

We return j + 1 as the length of the array with unique elements.
