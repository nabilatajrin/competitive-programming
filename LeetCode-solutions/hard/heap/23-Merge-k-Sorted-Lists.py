# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(h, (i.val, i))
        while h:
            node = heapq.heappop(h)[1]
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))
        return head.next
    
    
    #solution 2: fixed heapq
    def mergeKLists_heapq(self, lists):
        h = []
        head = tail = ListNode(0)
        for i in range(len(lists)):
            heapq.heappush(h, (lists[i].val, i, lists[i]))
        while h:
            node = heapq.heappop(h)
            node = node[2]
            tail.next = node
            tail = tail.next
            if node.next:
                i+=1
                heapq.heappush(h, (node.next.val, i, node.next))
        return head.next
        
