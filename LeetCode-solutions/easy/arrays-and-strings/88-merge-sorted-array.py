Easy | Facebook|35,Microsoft|10,Amazon|8,Bloomberg|3,Walmart Labs|3,IBM|3,Oracle|3,Apple|2,LinkedIn|2,Goldman Sachs|2,Yandex|2,Wish|2

LeetCode: https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
 
Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
-----------------------------------------------------------------------------------------------------------------------------------------------------
Solution:

Approach 1 : Merge and sort
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()


Approach 2 : Three Pointers (Start From the Beginning)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m] 
        
        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


Approach 3 : Three Pointers (Start From the End)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

---------------------------------
Approach 4 : Four Pointers
def merge(nums1, m, nums2, n):
    # Starting from the end of both arrays.
    p1, p2, p = m - 1, n - 1, m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, we copy them to nums1.
    nums1[:p2 + 1] = nums2[:p2 + 1]
------------------
Explanation:
The function merge takes four parameters: nums1, m, nums2, and n. nums1 represents the first sorted array with space to accommodate all elements, m is the number of elements in nums1, nums2 represents the second sorted array, and n is the number of elements in nums2 to be merged.

We create three pointers, p1, p2, and p, initialized to the end of nums1, the end of nums2, and the end of the space available in nums1 (after m elements), respectively.

We start a loop that runs while both p1 and p2 are greater than or equal to 0.

Inside the loop, we compare the elements at the positions p1 and p2 in nums1 and nums2, respectively.

If the element at nums1[p1] is greater than or equal to the element at nums2[p2], we place the nums1[p1] element in the available position p in nums1, and then move p1 one step back.

If the element at nums1[p1] is smaller than the element at nums2[p2], we place the nums2[p2] element in the available position p in nums1, and then move p2 one step back.

After placing an element in nums1, we decrement the p pointer.

We repeat this process until we have merged all elements from nums2 into nums1.

If there are any remaining elements in nums2 after the loop (i.e., p2 >= 0), we copy them to the beginning of nums1 since there is enough space for them.

By the end of this function, nums1 will contain the merged and sorted elements of both nums1 and nums2.
