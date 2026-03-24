# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
       total = 0
       def dfs(currNode , gp, p):
          nonlocal total
          if not currNode:
            return
          if gp and gp % 2 == 0:
            total += currNode.val
          dfs(currNode.left , p , currNode.val)
          dfs(currNode.right , p , currNode.val)
       dfs(root , None , None)
       return total


          
