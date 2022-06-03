# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Solution 1: If both lists are non-empty, I first make sure a starts smaller, use its head as result, and merge the             remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
    
    #Solution 2: First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the           remainders behind a.
    def mergeTwoLists(self, a, b):
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a
