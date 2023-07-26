LeetCode: https://leetcode.com/problems/contains-duplicate/

Solution 1:
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

Solution 3:
def containsDuplicate(self, nums: List[int]) -> bool:
        # Imagine we are hosting a party and checking for duplicate guests! 🎉👥

        unique_guests = set()  # This set will help us keep track of the unique guests.

        for num in nums:
            if num in unique_guests:
                # Oops! The guest has already arrived! We found a duplicate.
                return True
            else:
                # Yay! The guest is new. Let's welcome them to the party.
                unique_guests.add(num)

        # Hooray! Everyone at the party is unique. No duplicates found!
        return False

Explanation:
1. The function contains_duplicate takes a list nums as input, representing an array of integers (party guests).
2. It starts by imagining that you are hosting a party and checking for duplicate guests! 🎉👥 The guests in this scenario are the numbers in the nums list.
3. It uses a set called unique_guests to keep track of the unique guests who have arrived at the party so far.
4. The function then goes through each num in the nums list.
5. If the num (guest) is already in the unique_guests set, it means the guest has already arrived at the party, and we found a duplicate! So, the function immediately returns True.
6. If the num (guest) is not in the unique_guests set, it means the guest is new and unique! So, we add them to the unique_guests set to welcome them to the party.
7. After looping through all the guests (numbers), if no duplicates were found, the function returns False, indicating that all the guests at the party are unique.
