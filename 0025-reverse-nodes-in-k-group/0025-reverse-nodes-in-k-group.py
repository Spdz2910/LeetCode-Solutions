# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        node = head
        while count < k and node:
            node = node.next
            count +=1
        if count < k:
            return head
        #Đảo ngược đoạn con 
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #Gọi đệ quy dao ngược đoạn con 
        head.next = self.reverseKGroup(curr , k)
        return prev

