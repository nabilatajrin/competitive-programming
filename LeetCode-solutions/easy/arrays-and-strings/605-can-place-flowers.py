#LeetCode: https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

------------
Solution 01:
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
        return True

        # Since the first and last plots can be adjacent to a boundary,
        # we'll pad the flowerbed with zeros at the beginning and end.
        flowerbed = [0] + flowerbed + [0]
    
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                # Yay! We found an empty plot to plant a flower.
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
    
        # Oops! We couldn't plant all the flowers we wanted.
        return False
------------
Explanation:
1. The function plant_flowers takes two parameters: flowerbed, which is a list representing the flowerbed with 0s and 1s, and n, 
  which is the number of flowers we want to plant in the empty plots.
2. The function starts with a simple check. If n is 0, it means we don't need to plant any flowers, so we can return True immediately.
3. To handle the boundary cases, we pad the flowerbed list with 0s at the beginning and end. This is because the first and last plots 
  can potentially have only one neighbor, and we don't need to check for adjacent flowers there.
4. We then loop through the flowerbed list from the second element (index 1) to the second-to-last element (index len(flowerbed) - 2). 
  This is because we have added padding, and we need to avoid considering those padded elements in the loop.
5. Inside the loop, we check three conditions:
     a) flowerbed[i] == 0: This ensures that the current plot is empty, so we can plant a flower there.
     b) flowerbed[i - 1] == 0: This ensures that the previous plot is also empty, satisfying the no-adjacent-flowers rule.
     c) flowerbed[i + 1] == 0: This ensures that the next plot is empty too, again satisfying the no-adjacent-flowers rule.
6. If all three conditions are met, it means we found an empty plot where we can plant a flower. So, we update the flowerbed list to 
  plant a flower in that plot by setting flowerbed[i] = 1.
7. We then decrement the n variable since we have planted a flower, indicating that we have one less flower to plant.
8. If n becomes 0 at any point during the loop, it means we have successfully planted all the flowers we wanted, so we return True.
9. If we complete the loop and still have some flowers left to plant (i.e., n > 0), it means we couldn't plant all the flowers due 
  to the no-adjacent-flowers rule. In this case, we return False.
10. After the loop, the function returns either True (if all flowers were successfully planted) or False (if there wasn't enough space 
  to plant all the flowers).
11. The code then demonstrates how to use the plant_flowers function by creating a flowerbed and specifying the number of flowers we want 
  to plant. It prints a message accordingly, indicating whether we were able to plant all the flowers or not.

------------
Solution 02:
    def canPlaceFlowers(self, flowerbed, n):
        zeros, ans = 1, 0  # Easier handling of prefixes, just initialize zeros to 1
        for f in flowerbed:
            if f == 0: 
                zeros += 1
            else:
                ans += (zeros - 1) // 2
                zeros = 0
        return ans + zeros // 2 >= n  # Note that suffix zeros need not -1
    
------------    
Solution 03:
    def canPlaceFlowers(self, F, n):
        return sum((len(zeros) - 1) // 2 for zeros in ''.join(map(str, [0] + F + [0])).split('1')) >= n
