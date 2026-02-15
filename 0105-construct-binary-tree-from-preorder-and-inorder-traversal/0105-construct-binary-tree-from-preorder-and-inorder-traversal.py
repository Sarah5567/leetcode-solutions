# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def build_sub_tree(pre_idx: int, in_idx: int, border=float('inf')) -> tuple[Optional[TreeNode], int, int]:
            if pre_idx >= n or in_idx >= n:
                return None, pre_idx, in_idx

            if inorder[in_idx] == border:
                return None, pre_idx, in_idx + 1

            root_val = preorder[pre_idx]
            node = TreeNode(root_val)

            if inorder[in_idx] != root_val:
                node.left, pre_idx, in_idx = build_sub_tree(pre_idx + 1, in_idx, root_val)
            else:
                in_idx += 1
                pre_idx += 1

            node.right, pre_idx, in_idx = build_sub_tree(pre_idx, in_idx, border)

            return node, pre_idx, in_idx

        tree, _, _ = build_sub_tree(0, 0)
        return tree