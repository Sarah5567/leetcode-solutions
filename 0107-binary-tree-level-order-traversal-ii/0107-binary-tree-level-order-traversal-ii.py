# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
            
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            if len(ans) <= level:
                ans.append([])
            ans[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        height = len(ans)
        for i in range(height // 2):
            ans[i], ans[height - i - 1] = ans[height - i - 1], ans[i]

        return ans