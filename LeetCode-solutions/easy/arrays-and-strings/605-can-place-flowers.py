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

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False

-------------
Solution 02:

if not flowerbed[i]==0:
            i+=1
            continue
        elif i==0:
            if i+1 <=length:
                if flowerbed[i+1]==0:
                    spot_found = True
            else:
                spot_found = True
        elif i==length:
            if not i-1 < 0:
                if flowerbed[i-1] == 0:
                    spot_found = True
            else:
                spot_found = True
        else:
            if flowerbed[i-1] == flowerbed[i+1] == 0:
                spot_found = True
        
        if spot_found:
            spots+=1
            i+=2 # go to the next possible spot. Reserve this one
            if spots>=n:
                return True                
        else:
            i+=1 #go to the next possible spot. 
      
    return False
