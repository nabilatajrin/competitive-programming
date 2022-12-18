# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #The "proper" way:  
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
    
    #The "tupleify" way:
    def isSameTree(self, p, q):
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)
    
    #The first way as one-liner:
    def isSameTree(self, p, q):
        return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q
        
