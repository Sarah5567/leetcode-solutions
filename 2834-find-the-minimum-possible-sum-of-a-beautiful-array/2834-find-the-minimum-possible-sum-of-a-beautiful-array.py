class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        len1 = min(target // 2, n)
        total_sum = (1 + len1) * len1 // 2

        if len1 < n:
            len2 = n - len1
            total_sum += (target * 2 + len2 - 1) * len2 // 2

        return total_sum % 1000000007