# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k ==0:
            return head
        #Tính độ dài danh sách và tìm vị trí mới của đầu  danh sách 
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        k %=length # Số lần quay thực tế cần thực hiện
        if k ==0:
            return head
        #Tìm vị trí mới của đuôi danh sách và đầu danh sách
        tail_position = length - k - 1
        current = head 
        for _ in range(tail_position):
            current = current.next
        new_head = current.next
        current.next = None

        #Nối đuôi danh sách cũ với đầu danh sách cũ
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head

        return new_head


        