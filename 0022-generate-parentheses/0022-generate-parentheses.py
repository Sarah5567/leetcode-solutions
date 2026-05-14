class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recursion(parentheses, opens, cur_n):
            if cur_n == n and not opens:
                ans.append(''.join(parentheses))
                return 

            if opens:
                parentheses.append(')')
                recursion(parentheses, opens - 1, cur_n)
                parentheses.pop()

            if cur_n < n:
                parentheses.append('(')
                recursion(parentheses, opens + 1, cur_n + 1)
                parentheses.pop()

        parentheses = []
        recursion(parentheses, 0, 0)
        return ans
