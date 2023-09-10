# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # Biến instance để theo dõi nút hiện tại của linked list
        self.prev = None

        def flatten_helper(node):
            if not node:
                return

            # Lưu trữ right child trước để không bị mất
            right = node.right

            if self.prev:
                self.prev.right = node
                self.prev.left = None
            self.prev = node

            # Duyệt left và right child
            flatten_helper(node.left)
            flatten_helper(right)

        flatten_helper(root)
