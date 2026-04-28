class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        ops = []
        
        cur = 0
        for ch in expression:
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            else:
                nums.append(cur)
                ops.append(ch)
                cur = 0
        
        nums.append(cur)

        n = len(nums)

        dp = [[[] for _ in range(n)] for _ in range(n)]

        for i, num in enumerate(nums):
            dp[i][i].append(num)

        for col in range(1, n):
            for i, j in zip(range(n), range(col, n)):
                for k in range(i, j):
                    for left_val in dp[i][k]:
                        for right_val in dp[k + 1][j]:
                            match ops[k]:
                                case '+':
                                    dp[i][j].append(left_val + right_val)
                                case '-':
                                    dp[i][j].append(left_val - right_val)
                                case '*':
                                    dp[i][j].append(left_val * right_val)
        return dp[0][-1]




        

