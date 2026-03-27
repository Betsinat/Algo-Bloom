# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(order):
            if not order:
                return None
            root = TreeNode(order[0])
            i = 0
            while i < len(order) and order[i] <= order[0]:
                i += 1
            left = order[1:i]
            right = order[i:]
            root.left = helper(left)
            root.right = helper(right)

            return root
        return helper(preorder)