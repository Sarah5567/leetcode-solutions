class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ways = 0

        for length in range(1, int(math.sqrt(2 * n)) + 1):
            avg = n / length
            first_number = (2 * avg - length + 1) / 2
            if first_number >= 1 and first_number == int(first_number):
                ways += 1

        return ways
