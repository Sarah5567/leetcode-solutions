# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def handle_subtree(self, root: Optional[TreeNode]) -> TreeNode:
        right = root.right
        if root.left:
            root.right = root.left
            root.left = None
            root = self.handle_subtree(root.right)
        if right:
            root.right = right
            root = self.handle_subtree(right)

        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root:
            self.handle_subtree(root)
        