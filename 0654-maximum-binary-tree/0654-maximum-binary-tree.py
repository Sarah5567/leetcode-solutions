class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack[-1]
                stack.pop()

            if stack:
                stack[-1].right = node
            
            stack.append(node)

        return stack[0]
