import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        # Tạo một min-heap
        min_heap = []

        # Thêm nút đầu tiên mỗi danh sách liên kết vào min heap
        for list_head in lists:
            if list_head:
                heapq.heappush(min_heap, (list_head.val, id(list_head), list_head))

        # Tạo một nút giả và đặt nó làm nút hiện tại
        dummy = ListNode(0)
        current = dummy

        # Hợp nhất các danh sách liên kết sử dụng min-heap
        while min_heap:
            _, _, node = heapq.heappop(min_heap)

            # Gắn nút đã lấy ra vào con trỏ next của nút hiện tại
            current.next = node
            current = current.next

            # Nếu nút đã lấy ra có một nút tiếp theo, thêm nó vào min heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, id(node.next), node.next))

        # Trả về đầu của danh sách liên kết đã được hợp nhất và sắp xếp
        return dummy.next


