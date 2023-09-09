# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        # Tìm nút giữa danh sách
        mid = self.findMiddle(head)

        # Tạo nút cây tìm kiếm nhị phân với giá trị nút giữa
        root = TreeNode(mid.val)

        if head == mid:
            # Danh sách chỉ có 1 phần tử
            return root
        # Đệ quy chuyển đổi phần trái và phần phải thành cây BST
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root 

    def findMiddle(self,head):
        prev_ptr = None
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr  = fast_ptr.next.next
        
        if prev_ptr:
            prev_ptr.next = None

        return slow_ptr

