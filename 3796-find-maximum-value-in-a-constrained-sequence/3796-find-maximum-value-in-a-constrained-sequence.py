class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        INF = float('inf')

        left = [INF] * n
        right = [INF] * n

        for idx, max_value in restrictions:
            left[idx] = right[idx] = max_value

        left[0] = right[0] = 0

        for i in range(1, n):
            prev = left[i - 1] + diff[i - 1]
            if prev < left[i]:
                left[i] = prev

        for i in range(n - 2, -1, -1):
            prev = right[i + 1] + diff[i]
            if prev < right[i]:
                right[i] = prev

        ans = 0

        for i in range(n):
            val = left[i]
            if right[i] < val:
                val = right[i]

            if val > ans:
                ans = val

        return ans
