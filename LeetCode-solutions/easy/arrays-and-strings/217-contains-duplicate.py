Understand the Problem: In this problem, we're given a binary tree, and we need to swap the left and right subtrees of every node in the tree.

Think of a Simple Example: Let's consider a simple binary tree with just one node:

markdown
Copy code
    1
After swapping, it will remain the same because it has no left or right subtree.

Find a Strategy: To solve this problem, we can use a recursive approach. We'll start from the root of the tree and swap its left and right subtrees. Then, we'll recursively do the same for the left and right subtrees.

Explain the Code:

python
Copy code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:  # Base case: if the root is None, there's nothing to swap.
        return None
    
    # Swap the left and right subtrees of the current node.
    root.left, root.right = root.right, root.left
    
    # Recursively swap the left and right subtrees of the current node.
    invertTree(root.left)
    invertTree(root.right)
    
    return root  # Return the root of the inverted tree.

# Let's create a sample tree to test our function
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Test the function
new_root = invertTree(root)
Run Through the Code with an Example: We start at the root node, which is 1. We swap its left and right subtrees, so the tree becomes:

markdown
Copy code
    1
   / \
  3   2
Then, we recursively call invertTree for the left subtree (which is now 3) and the right subtree (which is now 2). This process continues until we reach the leaves of the tree.

Explain the Output: After swapping the left and right subtrees of every node in the tree, we get the inverted tree. The output here is not printed, but you would get the inverted tree in new_root.

So, in simple terms, we're flipping the tree upside down, swapping the left and right subtrees of each node, starting from the root and going all the way down to the leaves.


---------------------------------------------------------------------------------------------------------------------------------------------------------
Understand the Problem: In this problem, we're given an array of numbers, and we need to find out if there are any duplicates in the array.

Think of a Simple Example: Let's say we have an array [1, 2, 3, 4, 1]. Here, 1 appears twice, so the answer should be True, indicating that there are duplicates.

Find a Strategy: One simple way to solve this is by using a set. We can iterate through the array, adding each element to the set. If we encounter an element that's already in the set, it means we've found a duplicate.

Explain the Code:

python
Copy code
def containsDuplicate(nums):
    num_set = set()  # Create an empty set to store unique numbers.
    
    for num in nums:  # Iterate through each number in the array.
        if num in num_set:  # If the number is already in the set, it's a duplicate.
            return True
        else:
            num_set.add(num)  # Otherwise, add it to the set.
    
    return False  # If we reach here, it means there are no duplicates.

# Test the function
nums = [1, 2, 3, 4, 1]
print(containsDuplicate(nums))  # Output should be True
Run Through the Code with an Example: We start with an empty set. Then, we go through each number in the array. If we find a number that's already in the set, it means it's a duplicate, so we return True. Otherwise, we add the number to the set. If we go through the whole array without finding any duplicates, we return False.

Explain the Output: The output is True, indicating that there are duplicates in the array.

So, in simple terms, we're checking if there are any numbers that appear more than once in the array. We use a set to keep track of the numbers we've seen, and if we find a number that's already in the set, it means we've found a duplicate.

-------------------------------------------------------------------------------------------------------------------------------------------
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
