# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recur(arr):
            if not arr:
                return None
            i = len(arr) // 2
            curr = TreeNode(arr[i])
            curr.left = recur(arr[:i])
            curr.right = recur(arr[i+1:])
            return curr
        return recur(nums)
