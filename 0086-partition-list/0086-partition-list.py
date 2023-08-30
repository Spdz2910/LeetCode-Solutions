# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self,head, x):
        smaller_head = ListNode()       # Danh sách các nút có giá trị nhỏ hơn x
        greater_head = ListNode()       # Danh sách các nút có giá trị lớn hơn x
        smaller_tail = smaller_head     # Con trỏ đến cuối danh sách các nút nhỏ hơn x
        greater_tail = greater_head     # Con trỏ đến cuối danh sách các nút lớn hơn hoặc bằng x

        current = head  # Trỏ đến nút hiện tại đang xem xét

        while current:
            if current.val < x:
                # Nếu giá trị nhỏ hơn x, thêm vào danh sách nhỏ hơn
                smaller_tail.next = current
                smaller_tail = current
            else:
                # Nếu giá trị lớn hơn hoặc bằng x, thêm vào danh sách lớn hơn
                greater_tail.next = current
                greater_tail = current

            current = current.next  # Di chuyển đến nút tiếp theo trong danh sách gốc

        greater_tail.next = None  # Đảm bảo kết thúc danh sách lớn hơn
        smaller_tail.next = greater_head.next  # Kết nối danh sách nhỏ hơn và danh sách lớn hơn

        return smaller_head.next  # Trả về đầu danh sách đã sắp xếp