class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        left = [float('inf')] * n
        right = [float('inf')] * n

        for idx, max_value in restrictions:
            left[idx] = right[idx] = max_value

        left[0] = right[0] = 0

        for i in range(1, n):
            left[i] = min(left[i], left[i - 1] + diff[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i], right[i + 1] + diff[i])

        max_value = float('-inf')

        for left_value, right_value in zip(left, right):
            max_value = max(max_value, min(left_value, right_value))

        return max_value