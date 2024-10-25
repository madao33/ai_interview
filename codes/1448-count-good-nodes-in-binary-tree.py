# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root, maxV):
            if root == None:
                return 0
            ans = 0
            if root.val >= maxV:
                maxV = root.val
                ans += 1
            return ans + dfs(root.left, maxV) + dfs(root.right, maxV)
        return dfs(root, -10**5)
