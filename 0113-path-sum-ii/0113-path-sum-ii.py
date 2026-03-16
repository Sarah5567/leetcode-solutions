class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        def dfs(node, curr_sum, path):
            if not node:
                return []
            
            path.append(node.val)
            res = []

            if not node.left and not node.right and curr_sum + node.val == targetSum:
                res.append(path.copy())
            else:
                res.extend(dfs(node.left, curr_sum + node.val, path))
                res.extend(dfs(node.right, curr_sum + node.val, path))
            
            path.pop()
            return res

        return dfs(root, 0, [])