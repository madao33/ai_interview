# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, is_right, length):
            if root == None:
                return length
            if is_right:
                return max(dfs(root.left, False, length + 1), dfs(root.right, True, 1)) 
            else:
                return max(dfs(root.right, True, length + 1), dfs(root.left, False, 1))
        if root == None:
            return 0
        
        return dfs(root, True, 0) - 1

        