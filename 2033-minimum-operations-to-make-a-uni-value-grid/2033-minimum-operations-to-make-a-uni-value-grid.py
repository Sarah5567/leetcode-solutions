class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [element for row in grid for element in row]
        n = len(flat)

        if any((flat[i] - flat[i - 1]) % x for i in range(1, n)):
            return -1

        flat.sort()
        median = flat[n // 2]

        return sum(abs(element - median) // x for element in flat)
