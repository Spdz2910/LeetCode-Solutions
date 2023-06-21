class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def removeNthFromEnd(head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        # Di chuyển fast pointer n bước trước slow pointer
        for _ in range(n + 1):
            fast = fast.next

        # Di chuyển cả fast và slow pointer đến khi fast pointer đạt đến cuối danh sách
        while fast:
            fast = fast.next
            slow = slow.next

        # Xóa node bằng cách cập nhật liên kết của node trước node cần xóa
        slow.next = slow.next.next

        return dummy.next

