class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_nodes(node):
            p_found = node == p
            q_found = node == q

            if not node:
                return p_found, q_found, None

            p_found_left, q_found_left, ancestor = find_nodes(node.left)
            p_found |= p_found_left
            q_found |= q_found_left

            if p_found and q_found:
                return p_found, q_found, ancestor or node

            p_found_right, q_found_right, ancestor = find_nodes(node.right)
            p_found |= p_found_right
            q_found |= q_found_right

            if p_found and q_found and not ancestor:
                ancestor = node

            return p_found, q_found, ancestor

        _, _, ancestor = find_nodes(root)
        return ancestor
  