# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recursion(node):
            if not node:
                return 0, 0

            total1, fectorial1 = recursion(node.left)
            total2, fectorial2 = recursion(node.right)

            fectorial = max(fectorial1 + fectorial2, 1)

            next_total = total1 + total2 + node.val * fectorial
            next_fectorial = fectorial * 10

            return next_total, next_fectorial

        total, _ = recursion(root)
        return total
