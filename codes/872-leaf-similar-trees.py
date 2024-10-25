# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaf(self, root: Optional[TreeNode], res: list):
        if root.left == None and root.right == None:
            res.append(root.val)
        if root.left != None:
            self.getLeaf(root.left, res)
        if root.right != None:
            self.getLeaf(root.right, res)


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = [], []
        self.getLeaf(root1, leaf1)
        self.getLeaf(root2, leaf2)
        if len(leaf1) != len(leaf2):
            return False
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True