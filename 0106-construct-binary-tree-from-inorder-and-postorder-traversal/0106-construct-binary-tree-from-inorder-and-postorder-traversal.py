class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_indexes = {}
        for idx, num in enumerate(inorder):
            in_indexes[num] = idx

        post_indexes = {}       
        for idx, num in enumerate(postorder):
            post_indexes[num] = idx

        def build_node(in_left, in_right, cur_post):
            cur_val = postorder[cur_post]
            cur_in = in_indexes[cur_val]
            node = TreeNode(cur_val)
            if cur_post == 0:
                return node, -1

            next_post = cur_post - 1
            next_val = postorder[next_post]
            next_in = in_indexes[next_val]

            if in_left <= next_in <= in_right:
                if next_in > cur_in:
                    node.right, next_in = build_node(cur_in + 1, in_right, cur_post - 1)

            if in_left <= next_in <= in_right:
                next_post = post_indexes[inorder[next_in]]
                node.left, next_in = build_node(in_left, cur_in - 1, next_post)

            return node, next_in

        root, _ = build_node(0, len(inorder) - 1, len(postorder) - 1)
        return root
            