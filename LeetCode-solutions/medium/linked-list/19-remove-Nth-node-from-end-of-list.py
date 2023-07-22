# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #solution 1: Index and Remove
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]
    
    #solution 2: 
    def removeNthFromEnd(self, head, n):
        def remove(head, n):            
            if head == None: return head, 0
            node, count = remove(head.next, n)
            count += 1
            head.next = node
            if count == n: head = head.next
            return head, count
        return remove(head, n)[0]
