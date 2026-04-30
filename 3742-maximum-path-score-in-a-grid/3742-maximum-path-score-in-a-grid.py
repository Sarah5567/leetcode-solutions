from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # אופטימיזציה: אין טעם לבצע יותר מ-k איטרציות מאורך המסלול המקסימלי
        k = min(k, m + n - 1)

        # הקצאת זיכרון חד-פעמית
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if (i > 0 and dp[i - 1][j] == 0) or (j > 0 and dp[i][j - 1] == 0):
                        dp[i][j] = 0

        max_score = dp[-1][-1]
        
        prev = [[-1] * n for _ in range(m)]

        for _ in range(k):
            prev, dp = dp, prev
            
            for i in range(m):
                for j in range(n):
                    dp[i][j] = -1 
                    
                    val = grid[i][j]
                    is_zero = (val == 0)
                    current_max = -1

                    if i > 0:
                        if prev[i - 1][j] > current_max:
                            current_max = prev[i - 1][j]
                        if is_zero and dp[i - 1][j] > current_max:
                            current_max = dp[i - 1][j]
                            
                    if j > 0:
                        if prev[i][j - 1] > current_max:
                            current_max = prev[i][j - 1]
                        if is_zero and dp[i][j - 1] > current_max:
                            current_max = dp[i][j - 1]

                    if current_max != -1:
                        dp[i][j] = current_max + val

            if dp[-1][-1] > max_score:
                max_score = dp[-1][-1]

        return max_score