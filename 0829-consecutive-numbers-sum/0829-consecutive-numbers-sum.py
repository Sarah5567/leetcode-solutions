class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ways = 0
        k = 1
        tri = 0

        while tri < n:
            if (n - tri) % k == 0:
                ways += 1

            k += 1
            tri += k - 1

        return ways
