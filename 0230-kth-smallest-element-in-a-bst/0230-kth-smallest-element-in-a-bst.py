class Solution:
    def get_kth_smallest(self, node: Optional[TreeNode], idx: int, k: int) -> tuple(int, int):
        if not node:
            return idx, -1
        idx, ans = self.get_kth_smallest(node.left, idx, k)

        if idx > k:
            return idx + 1, ans
        elif idx == k:
            return idx + 1, node.val
        else:
            return self.get_kth_smallest(node.right, idx + 1, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx, ans = self.get_kth_smallest(root, 1, k)
        return ans