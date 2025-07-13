class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        first_max_so_far = [0] * n
        first_max_so_far[0] = height[0]
        for i in range(1, n):
            first_max_so_far[i] = max(height[i], first_max_so_far[i - 1])

        second_max_so_far = [0] * n
        second_max_so_far[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            second_max_so_far[i] = max(height[i], second_max_so_far[i + 1])

        total = 0
        for i in range(n):
            total += min(first_max_so_far[i], second_max_so_far[i]) - height[i]

        return total