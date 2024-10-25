# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        queue = deque()
        queue.append(root)
        while len(queue) is not 0:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                # 如果是这一层最后一个节点，为右视图的节点
                if i == length - 1:
                    ans.append(node.val)
        return ans