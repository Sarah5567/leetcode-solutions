class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ways = 0

        k = 1
        while k * (k - 1) // 2 < n:
            remainder = n - k * (k - 1) // 2

            if remainder % k == 0:
                a = remainder // k
                if a > 0:
                    ways += 1

            k += 1

        return ways