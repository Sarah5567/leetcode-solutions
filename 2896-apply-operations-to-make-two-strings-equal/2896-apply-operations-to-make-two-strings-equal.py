class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)

        diffs = []
        for i in range(n):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) % 2 == 1:
            return -1

        prev1 = x
        prev2 = 0
        for i in range(1, len(diffs)):
            cur_cost = min((diffs[i] - diffs[i - 1]) * 2 + prev2, prev1 + x)
            prev1, prev2 = cur_cost, prev1

        return prev1 // 2 if len(diffs) else 0
        