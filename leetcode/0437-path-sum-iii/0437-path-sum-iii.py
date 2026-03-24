class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        a = self.ps(root, targetSum)
        b = self.pathSum(root.left, targetSum)
        c = self.pathSum(root.right, targetSum)
        
        return a + b + c

    def ps(self, node, currentSum):
        if not node:
            return 0
        
        cnt = 0
        if node.val == currentSum:
            cnt += 1
        cnt += self.ps(node.left, currentSum - node.val)
        cnt += self.ps(node.right, currentSum - node.val)
        
        return cnt
        