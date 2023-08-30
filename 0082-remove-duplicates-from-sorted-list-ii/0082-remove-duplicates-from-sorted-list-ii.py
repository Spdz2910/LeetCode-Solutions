# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0) # Nút giả kiểm tra danh sách có rỗng không
        dummy.next = head
        current = dummy

        while current.next and current.next.next: # duyệt qua nút hiện tại vs nút kế tiếp
            if current.next.val == current.next.next.val: #Kiểm tra giá trị  2 nút có = nhau ko
                duplicate_val = current.next.val #Lưu trữ các nút trùng lặp
                #Duyêt qua các nút trùng lặp liên típ là loại bỏ
                while current.next and current.next.val == duplicate_val:
                    current.next = current.next.next
            else:
                    current = current.next # Không có nút trùng , di chuyển con trỏ tiếp theo
        return dummy.next
                 


