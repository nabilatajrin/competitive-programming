# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Naive approach, O(|s| * |t|)
    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and 
                self.isMatch(s.left, t.left) and 
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t) -> bool:
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
