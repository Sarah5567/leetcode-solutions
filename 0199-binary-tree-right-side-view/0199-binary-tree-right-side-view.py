# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            if not node:
                continue

            if level == len(view):
                view.append(node.val)
            else:
                view[level] = node.val

            q.append((node.left, level + 1))
            q.append((node.right, level + 1))

        return view