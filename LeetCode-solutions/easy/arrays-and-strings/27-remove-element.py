#LeetCode: https://leetcode.com/problems/remove-element/

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
 
Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

-----------------------------
Solution:
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count
-----------------------------
runtime : 32 ms, beats 73.16%
memory usage: 13.9 mb, beats 99.92%    
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            i +=1 
        return len(nums)
-----------------------------
rumtime: 32 ms

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while (i < length):
            if nums[i] == val:
                nums.remove(nums[i])
                length -= 1
                continue
            i += 1
        return len(nums)

--------------------------
Solution:
def remove_element(nums, val):
    i = 0  # Pointer to iterate the array.

    for num in nums:
        if num != val:
            nums[i] = num
            i += 1

    return i

Explanation:
The function remove_element takes a list nums and a value val as input.
We use a pointer i to iterate through the array.
We loop through the elements in the array using a for loop.
If the current element num is not equal to the given value val, it means we want to keep this element in the modified array. So, we copy it to the position indicated by i in the original array and increment i by 1.
We repeat this process until we have processed all the elements in the array.
After the loop, i will be the index of the last element in the modified array.
We return i, which represents the new length of the array after removing all instances of val.
