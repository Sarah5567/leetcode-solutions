class Solution:
    def lastRemaining(self, n: int) -> int:
        remaining = n
        size = 1
        left = True
        first = 1

        while remaining > 1:
            if left or remaining % 2:
                first += size
            remaining  //= 2
            size *= 2
            left = not left

        return first
