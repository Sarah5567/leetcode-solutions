class Solution:
    def subtree_findings(self, node, p, q):
        # returns: (p_exists, q_exists, ans)
        if not node:
            return False, False, None

        lp, lq, lans = self.subtree_findings(node.left, p, q)
        if lans:
            return True, True, lans

        rp, rq, rans = self.subtree_findings(node.right, p, q)
        if rans:
            return True, True, rans

        p_exists = lp or rp or node is p
        q_exists = lq or rq or node is q

        ans = node if p_exists and q_exists else None
        return p_exists, q_exists, ans

    def lowestCommonAncestor(self, root, p, q):
        return self.subtree_findings(root, p, q)[2]
