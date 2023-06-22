class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def mergeTwoLists(list1, list2):
        # Xử lý trường hợp danh sách trống
        if not list1:
            return list2
        if not list2:
            return list1

        # Chọn node đầu tiên trong danh sách có giá trị nhỏ hơn
        if list1.val <= list2.val:
            merged = list1
            list1 = list1.next
        else:
            merged = list2
            list2 = list2.next

        # Duyệt qua cả hai danh sách và hợp nhất các node theo thứ tự tăng dần
        current = merged
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Nối danh sách còn lại
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return merged


