# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        maxSum = -10**6
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            tempSum = 0
            length = len(queue)
            depth += 1
            for i in range(length):
                node = queue.popleft()
                tempSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if tempSum > maxSum:
                maxSum = tempSum
                ans = depth
        return ans
