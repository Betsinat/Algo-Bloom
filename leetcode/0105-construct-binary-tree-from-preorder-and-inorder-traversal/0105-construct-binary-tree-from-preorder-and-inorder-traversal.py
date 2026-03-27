# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(porder, iorder):
            if not porder or not iorder:
                return None
            root = TreeNode(porder[0])
            i = iorder.index(root.val)
            leftp = porder[1:i + 1]
            rightp = porder[i+1:]
            root.left = helper(leftp, iorder[:i])
            root.right = helper(rightp, iorder[i+1:])
            return root
        return helper(preorder,inorder)