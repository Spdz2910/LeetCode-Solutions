# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        tortoise = head
        hare = head.next
        
        while tortoise != hare:
            if not hare or not hare.next:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
        return True
        
        